import pandas as pd
import os

def load_data(age_group):
    """
    Load and preprocess the data for the specified age group.
    - Reads and cleans the data files from the specified folder.
    - Merges the data into a single DataFrame.
    Args:
        age_group (str): The folder name corresponding to the age group (e.g., '15_49', '15_24').
    Returns:
        pd.DataFrame: A cleaned and merged DataFrame for the selected age group.
    """
    # Define the folder path based on the selected age group
    folder_path = f'data/{age_group}'
    
    # File paths
    api_path = os.path.join(folder_path, 'API.csv')
    country_path = os.path.join(folder_path, 'Metadata_Country.csv')
    indicator_path = os.path.join(folder_path, 'Metadata_Indicator.csv')
    
    # Load datasets
    df_api = pd.read_csv(api_path, skiprows=4)
    df_country = pd.read_csv(country_path)
    df_indicator = pd.read_csv(indicator_path)

    # Drop unnecessary columns
    df_api = df_api.drop(columns=['Unnamed: 68'], errors='ignore')  # Remove unnecessary column
    df_country = df_country.drop(columns=['Unnamed: 5'], errors='ignore')  # Remove unnecessary column
    df_indicator = df_indicator.drop(columns=['Unnamed: 4'], errors='ignore')  # Remove unnecessary column

    # Fill missing values
    df_api = df_api.fillna(0)
    df_country['Region'] = df_country['Region'].fillna('Unknown')
    df_country['IncomeGroup'] = df_country['IncomeGroup'].fillna('Unknown')
    df_indicator = df_indicator.fillna('Unknown')

    # Rename API dataset columns for clarity
    df_api.columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'] + [str(year) for year in range(1960, 2024)]

    # Convert year columns to numeric values
    for year in range(1960, 2024):
        df_api[str(year)] = pd.to_numeric(df_api[str(year)], errors='coerce')

    # Merge the datasets
    df_api_country = df_api.merge(df_country[['Country Code', 'Region', 'IncomeGroup']], on='Country Code', how='left')
    df_api_complete = df_api_country.merge(df_indicator[['INDICATOR_CODE', 'INDICATOR_NAME']], left_on='Indicator Code', right_on='INDICATOR_CODE', how='left')

    # Drop redundant 'INDICATOR_CODE' column
    df_api_complete = df_api_complete.drop(columns=['INDICATOR_CODE'], errors='ignore')

    # Fill remaining missing values
    df_api_complete['Region'] = df_api_complete['Region'].fillna('Unknown')
    df_api_complete['IncomeGroup'] = df_api_complete['IncomeGroup'].fillna('Unknown')

    return df_api_complete