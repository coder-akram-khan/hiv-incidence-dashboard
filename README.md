# Global HIV Incidence Dashboard

An interactive and comprehensive dashboard for exploring global HIV incidence data. This application leverages Streamlit for web deployment, Plotly for data visualizations, and advanced analytics to provide insights into HIV trends across different regions, income groups, and age demographics.

![image alt](https://github.com/coder-akram-khan/hiv-incidence-dashboard/blob/main/assets/hiv.jpg?raw=true)

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Data Sources](#data-sources)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview
The Global HIV Incidence Dashboard visualizes historical HIV incidence data from 1960 to 2023 for different age groups (e.g., 15-49, 15-24). It provides a detailed breakdown by region, income group, and country, offering valuable insights for policymakers, researchers, and healthcare professionals.

---

## Features
- **Dynamic Filters:**
  - Age Group Selection
  - Indicator Selection
  - Year Range Filtering
- **Visualizations:**
  - Heatmaps
  - Bubble Charts
  - Pie Charts
  - Stacked Bar Charts
  - Choropleth Maps (Static and Animated)
  - Sunburst and Treemap Visualizations
  - Trend Charts
- **Interactive Features:**
  - Data download option for filtered datasets
  - Year slider for focused analysis
- **Statistical Summary:**
  - Highlights of highest, lowest, and average incidence rates for the selected year.

---

## Technologies Used
- **Languages & Libraries:**
  - Python
  - Streamlit
  - Plotly
  - Pandas
  - JSON
- **Tools:**
  - Streamlit Lottie for animations
  - Plotly for interactive visualizations

---

## Installation
### Prerequisites
Ensure you have Python 3.8 or above installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hiv-incidence-dashboard.git
   cd hiv-incidence-dashboard
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. Select an age group from the sidebar.
2. Apply filters like indicator and year.
3. Explore the visualizations and insights on the dashboard.
4. Download filtered data for offline analysis.

---

## File Structure
```plaintext
HIV_Incidence_Dashboard/
│
├── app.py                              # Main Streamlit application
├── requirements.txt                    # Python dependencies
├── README.md                           # Project overview and instructions
├── .gitignore                          # Files to be ignored by Git
│
├── data/                               # Directory for datasets
│   ├── 15_49/                          # Age group folder
│   │   ├── API.csv                     # HIV incidence data for 15-49 age group
│   │   ├── Metadata_Country.csv        # Country metadata
│   │   ├── Metadata_Indicator.csv      # Indicator metadata
│   ├── 15_24/                          # Additional age group folder
│       ├── API.csv                     # HIV incidence data for 15-24 age group
│       ├── Metadata_Country.csv        # Country metadata
│       ├── Metadata_Indicator.csv      # Indicator metadata
│
├── assets/                             # Directory for static assets
│   ├── hiv_logo.jpg                    # Project logo or other static images
│   ├── coder.json                      # Lottie animation file for coding theme
│   ├── doctor.json                     # Lottie animation file for medical theme
│
└── utils/                              # Utility scripts
    ├── __init__.py                     # Marks the directory as a Python module
    ├── data_preprocessing.py           # Functions for data loading and preprocessing

```

---

## Data Sources
The datasets are sourced from global health and statistics organizations, such as:
- **World Bank**
- **World Health Organization (WHO)**

Ensure proper credit is given to these sources if using this application for presentations or research.

---

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a meaningful commit message"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

### Developed with ❤️ by Akram Khan
- [LinkedIn](https://www.linkedin.com/in/mr-akram-khan/)
- [GitHub](https://github.com/coder-akram-khan)
