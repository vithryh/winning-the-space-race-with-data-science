# Falcon 9 First Stage Landing Success Prediction

## Overview

This repository contains a comprehensive presentation that predicts the success of Falcon 9 first stage landings, leveraging SpaceX's innovative and cost-effective launch model. The ability to reuse the first stage of the Falcon 9 rocket plays a critical role in reducing overall launch costs, making SpaceX a formidable competitor in the space launch industry.

## Key Highlights

- **Cost-Effective Launch Model:** SpaceX's approach to reusing the first stage significantly lowers launch costs to $62 million per launch, compared to $165 million for traditional launch providers.
- **Predictive Analysis:** By forecasting the success of Falcon 9 first stage landings, we can estimate future launch costs and assess the economic impact of reusability.
- **Strategic Insights:** Our analysis provides valuable insights for competitors and stakeholders bidding against SpaceX, helping them understand the cost advantages and operational efficiencies of the Falcon 9 launch model.

## Methodologies

1. **Data Collection:** Using SpaceX’s API and web scraping to gather comprehensive launch data.
2. **Data Wrangling:** Preprocessing and cleaning the collected data.
3. **Exploratory Data Analysis (EDA):** Using SQL for data querying and visualization tools for in-depth analysis.
4. **Interactive Visual Analytics:** Using Plotly Dash and Folium to map and explore data spatially.
5. **Machine Learning Prediction:** Developing models to predict the success of first-stage landings.

## Summary of Results

- **Exploratory Data Analysis:** Identified key features influencing launch success.
- **Interactive Visual Analytics:** Provided dynamic insights, enhancing understanding of data patterns.
- **Predictive Analysis:** Determined the most effective machine learning model, highlighting critical features for predicting landing success. This model forecasts launch costs accurately, offering a competitive edge to companies aiming to challenge SpaceX’s market position.

## Contents

- **Data Collection Notebooks:**
  - `1_data-collection-api.ipynb`
  - `1_data-collection-with-web-scraping.ipynb`
- **Data Wrangling Notebook:**
  - `2_data-wrangling.ipynb`
- **Exploratory Data Analysis Notebooks:**
  - `3_eda-with-sql.ipynb`
  - `3_eda-with-visualization.ipynb`
- **Interactive Visual Analytics:**
  - `4_interactive-dashboard-with-plotly-dash.py`
  - `4_interactive-visual-analytics-with-folium.ipynb`
- **Machine Learning Prediction Notebook:**
  - `5_machine-learning-prediction.ipynb`
- **Data Directory:**
  - `data`
- **Presentation:**
  - `Winning the Space Race with Data Science.pdf`

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vithryh/winning-the-space-race-with-data-science.git
   ```
2. **Explore the Presentation:**
   Open the presentation file (`Winning the Space Race with Data Science.pdf`) to review the key findings and insights.
3. **Analyze the Data:**
   Navigate to the `data` directory to explore the data sets used for the analysis.
4. **Run the Notebooks and Scripts:**
   Use the provided notebooks and scripts to replicate the analysis and predictions. Detailed instructions are provided within each notebook and script.

---

This repository aims to provide a thorough understanding of the economic and operational impacts of SpaceX's reusable launch model, offering valuable insights for industry stakeholders and enthusiasts alike.
