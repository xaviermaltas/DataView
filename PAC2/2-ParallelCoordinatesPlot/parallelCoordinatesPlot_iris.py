#python3 parallelCoordinatesPlot_iris.py
import plotly.express as px
import pandas as pd

# Load the Iris dataset from the 'iris.csv' file
df = pd.read_csv('iris.csv')

# Map the 'variety' column to numerical values
variety_mapping = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
df['variety_id'] = df['variety'].map(variety_mapping)

# Create a Parallel Coordinates plot
fig = px.parallel_coordinates(df, 
                              color="variety_id",
                              dimensions=['sepal.length', 'sepal.width', 'petal.length', 'petal.width'],
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=1)

# Save the plot as a PNG file
fig.write_image('parallelCoordinatesPlot_iris.png')

# Save the plot as an HTML file
fig.write_html('parallelCoordinatesPlot_iris.html')