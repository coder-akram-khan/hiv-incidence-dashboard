import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import json
from utils.data_preprocessing import load_data





# Sidebar for dataset selection
age_groups = ["15_49", "15_24"]  # Add more age groups if available
selected_age_group = st.sidebar.selectbox("Select Age Group", age_groups)

# Load the data for the selected age group
with st.spinner(f"Loading data for age group {selected_age_group}..."):
    df = load_data(selected_age_group)

# Title and description
st.title("Global HIV Incidence Dashboard")
st.markdown(
    f"""
    An interactive dashboard to explore global HIV incidence data for ages {selected_age_group.replace('_', '-')} 
    from 1960 to 2023.
    """
)

# Function to load Lottie animations locally
def load_lottie_local(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Lottie Animation
# Create two columns for animations
col1, col2 = st.columns(2, gap="medium")

# Load and display the left animation
with col1:
    lottie_animation_left = load_lottie_local("./assets/coder.json")
    if lottie_animation_left:
        st_lottie(lottie_animation_left, height=400, key="left_animation")

# Load and display the right animation
with col2:
    lottie_animation_right = load_lottie_local("./assets/doctor.json")  # Replace with a visually matching animation
    if lottie_animation_right:
        st_lottie(lottie_animation_right, height=400, key="right_animation")

# Add a connecting line or bridge between animations
st.markdown(
    """
    <div style="width: 100%; text-align: center; margin-top: -50px;">
        <hr style="border: none; height: 2px; background: linear-gradient(to right, #56CCF2, #2F80ED); margin: 0;">
    </div>
    """,
    unsafe_allow_html=True,
)


# Sidebar filters
st.sidebar.header("Filters")
indicator_options = df['Indicator Name'].unique()
indicator = st.sidebar.selectbox("Select an Indicator", indicator_options, index=0)
years = [str(year) for year in range(1960, 2024)]
year = st.sidebar.selectbox("Select Year", years, index=len(years) - 1)

# Filter data based on indicator
df_filtered = df[df['Indicator Name'] == indicator]

# Heatmap
heatmap_data = df_filtered[['Region'] + years].dropna()
heatmap_data = heatmap_data.melt(id_vars='Region', var_name='Year', value_name='Incidence Rate')
fig_heatmap = px.density_heatmap(
    heatmap_data,
    x='Year',
    y='Region',
    z='Incidence Rate',
    color_continuous_scale='Viridis',
    title="HIV Incidence Rates Across Regions and Years"
)
st.plotly_chart(fig_heatmap)

# Display filtered data
st.subheader(f"{indicator} - {year}")
df_year = df_filtered[['Country Name', year]].dropna()
df_year = df_year.rename(columns={year: "Incidence Rate"})
st.write(df_year)


# Bubble chart: Incidence rate by region/income group
fig_bubble = px.scatter(
    heatmap_data,
    x='Year',
    y='Region',
    size='Incidence Rate',
    color='Region',
    hover_name='Region',
    title="HIV Incidence Rate Bubble Chart"
)
st.plotly_chart(fig_bubble)

# Pie chart for income groups
income_data = df_year.merge(df_filtered[['Country Name', 'IncomeGroup']], on='Country Name', how='left')
income_data = income_data.groupby('IncomeGroup').agg({'Incidence Rate': 'mean'}).reset_index()

fig_pie = px.pie(
    income_data,
    values='Incidence Rate',
    names='IncomeGroup',
    title="Incidence Rate Distribution by Income Group",
    color_discrete_sequence=px.colors.sequential.Plasma
)
st.plotly_chart(fig_pie)

# Stacked bar chart for regions over time
stacked_bar_data = heatmap_data.groupby(['Year', 'Region'])['Incidence Rate'].mean().reset_index()

fig_stacked = px.bar(
    stacked_bar_data,
    x='Year',
    y='Incidence Rate',
    color='Region',
    title="HIV Incidence Rates by Region Over Time",
    barmode='stack'
)
st.plotly_chart(fig_stacked)

# Dynamic world map
fig_world_map = px.choropleth(
    df_year,
    locations="Country Name",
    locationmode="country names",
    color="Incidence Rate",
    hover_name="Country Name",
    color_continuous_scale=px.colors.sequential.Plasma,
    title=f"Global HIV Incidence Rate in {year}"
)
st.plotly_chart(fig_world_map)

# Animated world map
fig_animated = px.choropleth(
    df_filtered.melt(id_vars=['Country Name'], var_name='Year', value_name='Incidence Rate'),
    locations="Country Name",
    locationmode="country names",
    color="Incidence Rate",
    animation_frame="Year",
    color_continuous_scale='Plasma',
    title="Global HIV Incidence Rate Over Time"
)
st.plotly_chart(fig_animated)

# Sunburst Chart
if not df_year.empty:
    fig_sunburst = px.sunburst(
        df_year.merge(df_filtered[['Country Name', 'Region', 'IncomeGroup']], on='Country Name', how='left'),
        path=['Region', 'IncomeGroup', 'Country Name'],
        values='Incidence Rate',
        title="HIV Incidence Sunburst Chart"
    )
    st.plotly_chart(fig_sunburst)

# Treemap
if not df_year.empty:
    fig_treemap = px.treemap(
        df_year.merge(df_filtered[['Country Name', 'Region', 'IncomeGroup']], on='Country Name', how='left'),
        path=['Region', 'IncomeGroup', 'Country Name'],
        values='Incidence Rate',
        title="HIV Incidence Treemap"
    )
    st.plotly_chart(fig_treemap)

# Bar chart for income groups
income_data = df_year.merge(df_filtered[['Country Name', 'IncomeGroup']], on='Country Name', how='left')
income_data = income_data.groupby('IncomeGroup').agg({'Incidence Rate': 'mean'}).reset_index()
fig_income = px.bar(
    income_data,
    x='IncomeGroup',
    y='Incidence Rate',
    title=f"Average HIV Incidence Rate by Income Group in {year}",
    color='IncomeGroup'
)
st.plotly_chart(fig_income)

# Bar chart for regions
region_data = df_year.merge(df_filtered[['Country Name', 'Region']], on='Country Name', how='left')
region_data = region_data.groupby('Region').agg({'Incidence Rate': 'mean'}).reset_index()
fig_region = px.bar(
    region_data,
    x='Region',
    y='Incidence Rate',
    title=f"Average HIV Incidence Rate by Region in {year}",
    color='Region'
)
st.plotly_chart(fig_region)

# Trend Chart
df_trend = df_filtered[['Country Name'] + years].set_index('Country Name').T
df_trend = df_trend.reset_index().melt(id_vars='index', var_name='Country', value_name='Incidence Rate')
df_trend.columns = ['Year', 'Country', 'Incidence Rate']
fig_trend = px.line(df_trend, x='Year', y='Incidence Rate', color='Country', title=f"Trends of {indicator} Over Time")
st.plotly_chart(fig_trend)

import streamlit.components.v1 as components

# --- Statistical Summary Section ---
highest = df_year.loc[df_year['Incidence Rate'].idxmax()]
lowest = df_year.loc[df_year['Incidence Rate'].idxmin()]
avg_incidence = df_year['Incidence Rate'].mean()

# Customized container for statistical summary
st.markdown(f"""
    <style>
        .stat-card {{
            background-color: #f7f7f7;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        .stat-card h3 {{
            color: #ff6f61;
            margin-bottom: 5px;
        }}
        .stat-card p {{
            margin: 5px 0;
            font-size: 16px;
            color: #333;
        }}
    </style>
    <div class="stat-card">
        <h3>Statistical Summary for {year}</h3>
        <p><b>Highest Incidence Rate:</b> {highest['Country Name']} - {highest['Incidence Rate']}</p>
        <p><b>Lowest Incidence Rate:</b> {lowest['Country Name']} - {lowest['Incidence Rate']}</p>
        <p><b>Average Incidence Rate:</b> {avg_incidence:.2f}</p>
    </div>
""", unsafe_allow_html=True)

# --- Download Button ---
st.download_button(
    label="📥 Download Filtered Data",
    data=df_year.to_csv(index=False).encode('utf-8'),
    file_name="filtered_data.csv",
    mime='text/csv'
)

# --- Slider for Year Range ---
st.markdown("### Filter Data by Year Range")
year_range = st.slider("Select Year Range", min_value=1960, max_value=2023, value=(2000, 2020))
df_filtered_range = heatmap_data[
    (heatmap_data['Year'] >= str(year_range[0])) & 
    (heatmap_data['Year'] <= str(year_range[1]))
]

st.write(f"Filtered Data for Year Range: {year_range[0]} - {year_range[1]}")
st.dataframe(df_filtered_range)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p>Developed with ❤️ by <b>Akram Khan</b></p>
        <p>📫 Connect with me on <a href="https://www.linkedin.com/in/mr-akram-khan/" target="_blank">LinkedIn</a> | <a href="https://github.com/coder-akram-khan" target="_blank">GitHub</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)