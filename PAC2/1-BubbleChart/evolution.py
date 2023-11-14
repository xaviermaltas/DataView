import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('Life Expectancy vs GDP 1950-2018.csv')

# Create Dash app
app = dash.Dash(__name__)

# Set up the app layout
app.layout = html.Div([
    dcc.Graph(id='bubble-chart'),
    dcc.Slider(
        id='year-slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        step=1,
        marks={str(year): {'label': str(year) if year == df['Year'].min() else '', 'style': {'transform': 'rotate(-45deg)', 'white-space': 'nowrap'}} for year in df['Year'].unique()},
        value=df['Year'].min(),
    ),
    html.Div(id='slider-output-container', style={'margin-top': 20}),
])

# Define callback to update bubble chart and display the selected year
@app.callback(
    [Output('bubble-chart', 'figure'),
     Output('slider-output-container', 'children'),
     Output('year-slider', 'marks')],
    [Input('year-slider', 'value')]
)
def update_bubble_chart(selected_year):
    filtered_df = df[df['Year'] == selected_year]

    # Filter out NaN values from the 'size' column
    filtered_df = filtered_df.dropna(subset=['Population'])

    fig = px.scatter(
        filtered_df,
        x='GDP',
        y='Life expectancy',
        size='Population',
        color='Continent',
        hover_name='Country',
        log_x=True,
        size_max=60
    )

    fig.update_layout(
        title=f'Life Expectancy vs GDP Evolution for {selected_year}',
        xaxis_title='GDP',
        yaxis_title='Life Expectancy',
        showlegend=True,
        xaxis=dict(
            type='log',
            tickvals=[300, 1000, 3000, 10000, 20000, 30000, 40000, 50000, 60000, 80000, 100000, 120000, 150000, 200000],
            ticktext=['300', '1K', '3K', '10K', '20K', '30K', '40K', '50K', '60K', '80K', '100K', '120K', '150K', '200K']
        )
    )

    # Show label only for the currently selected year
    marks = {str(year): {'label': str(year) if year == selected_year else '', 'style': {'transform': 'rotate(-45deg)', 'white-space': 'nowrap'}} for year in df['Year'].unique()}
    
    return fig, '', marks

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
