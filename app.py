import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('task 2 Pink Morsels data.csv')


df.columns = df.columns.str.strip()


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')


df = df.sort_values(by='Date')


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsels Sales Data"),

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
