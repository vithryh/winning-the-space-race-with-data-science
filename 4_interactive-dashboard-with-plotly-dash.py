# Import required libraries
import numpy as np
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("data/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(
    children=[html.H1('SpaceX Launch Records Dashboard',
                      style={'textAlign': 'center', 'color': '#503D36',
                             'font-size': 40}),
              dcc.Dropdown(
                  id='site-dropdown',
                  options=[
                      {'label': 'All Sites', 'value': 'ALL'},
                      {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                      {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                      {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                      {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                  ],
                  value='ALL',
                  placeholder='Select a Launch Site here',
              ),
              html.Br(),

              html.Div(dcc.Graph(id='success-pie-chart')),
              html.Br(),

              html.P("Payload range (Kg):"),
              # TASK 3: Add a slider to select payload range
              dcc.RangeSlider(id='payload-slider',
                              min=0,
                              max=10000,
                              step=1000,
                              value=[min_payload, max_payload]
                              ),

              html.Div(dcc.Graph(id='success-payload-scatter-chart')),
              ])


@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class', 
                     names='Launch Site', 
                     title='Total Success Launches By Site')
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df, 
                     names='class', 
                     title=f'Success vs Failure for site {entered_site}')
    return fig


@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id="payload-slider", component_property="value")]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    
    if entered_site == 'ALL':
        filtered_df = spacex_df[mask]
        title = 'Correlation between Payload and Success for all Sites ({} kg to {} kg)'.format(low, high)
    else:
        filtered_df = spacex_df[mask & (spacex_df['Launch Site'] == entered_site)]
        title = f'Correlation between Payload and Success for site {entered_site} ({low} kg to {high} kg)'
    
    np.random.seed(9)
    y_jitter = filtered_df['class'] + np.random.normal(0, 0.02, size=len(filtered_df))
    
    fig = px.scatter(
        filtered_df, 
        x='Payload Mass (kg)', 
        y=y_jitter, 
        color='Booster Version Category',
        title=title,
        color_discrete_sequence=px.colors.qualitative.Plotly
    )

    fig.update_layout(
        xaxis=dict(
            range=[low-100, high+100],
            tickformat='d'
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=['0', '1'],
            title='Class',
            range=[-0.1, 1.1]
        ),
        title={
            'y': 0.85,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )
    fig.add_vline(x=low, line_width=1, line_dash="dash", line_color="black", opacity=0.5)
    fig.add_vline(x=high, line_width=1, line_dash="dash", line_color="black", opacity=0.5)

    # If no data points, add annotation
    if filtered_df.empty:
        fig.add_annotation(
            x=(low+high)/2,
            y=0.5,
            xref="x",
            yref="y",
            text="No data points in this range",
            showarrow=False,
            font=dict(size=16)
        )
    else:
        # Add jitter to y-axis for better visualization
        y_jitter = filtered_df['class'] + np.random.normal(0, 0.02, size=len(filtered_df))
        fig.data[0].y = y_jitter

        # Only add counts annotation if there are data points
        add_counts_annotation(fig, filtered_df)
    
    return fig


def add_counts_annotation(fig, filtered_df):
    if filtered_df.empty:
        return

    booster_outcomes = filtered_df.groupby('Booster Version Category')['class'].value_counts().unstack(fill_value=0)
    
    # Check if we have both success and failure outcomes
    if 0 not in booster_outcomes.columns:
        booster_outcomes[0] = 0
    if 1 not in booster_outcomes.columns:
        booster_outcomes[1] = 0
    
    booster_outcomes = booster_outcomes.rename(columns={0: 'Failures', 1: 'Successes'})
    booster_outcomes['Total'] = booster_outcomes['Failures'] + booster_outcomes['Successes']
    booster_outcomes = booster_outcomes.sort_values('Total', ascending=False)

    totals = booster_outcomes.sum().to_frame().T
    totals.index = ['Total']
    booster_outcomes_with_total = pd.concat([booster_outcomes, totals])
    
    annotation_text = " Booster Version Counts<br>   Success|Failure|Total<br>"
    annotation_text += "<br>".join([
        f"{booster:<5}| {row['Successes']:2d} | {row['Failures']:2d}    |   {row['Total']:2d}"
        for booster, row in booster_outcomes_with_total.iterrows()
    ])
    
    fig.add_annotation(
        xref="paper", yref="paper",
        x=1.02, y=0.5,
        text=annotation_text,
        showarrow=False,
        font=dict(size=12, family='monospace'),
        align="left",
        bordercolor="black",
        borderwidth=1,
        xanchor="left",
        yanchor="top"
    )
    

# Run the app
if __name__ == '__main__':
    app.run_server()
