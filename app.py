import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the preprocessed data (update the file path as needed)
df = pd.read_csv('task 2 Pink Morsels data.csv')

# Check column names and rename if necessary (remove extra whitespace)
df.columns = df.columns.str.strip()

# Ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Sort by Date for consistent plotting
df = df.sort_values(by='Date')

# Initialize Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # Header title for the app
    html.H1("Soul Foods Pink Morsels Sales Data"),

    # Line chart for sales over time
    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            df,
            x='Date',
            y='Sales',
            title='Sales of Pink Morsels Over Time',
            labels={'Date': 'Date', 'Sales': 'Total Sales ($)'}
        ).update_layout(
            shapes=[
                dict(
                    type="line",
                    x0="2021-01-15", x1="2021-01-15",
                    y0=0, y1=df['Sales'].max(),
                    line=dict(color="red", width=2, dash="dash"),
                )
            ],
            annotations=[
                dict(
                    x="2021-01-15", y=df['Sales'].max(),
                    xref="x", yref="y",
                    text="Price Increase",
                    showarrow=True,
                    arrowhead=1,
                    ax=0, ay=-40
                )
            ]
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
