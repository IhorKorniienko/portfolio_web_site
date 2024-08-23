import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

# Read the file
data = pd.read_csv('beer_reviews.csv', low_memory=False)

# Select only numerical columns for correlation
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix
corr_metrics = numeric_data.corr()

# Create a rounded strings array for annotations
annotations = corr_metrics.round(2).astype(str).values  # Annotations with 2 decimal points

# Combine the annotation texts with the numeric values for display
# If you want a specific format like "0.56" for the value
z_text = corr_metrics.round(2).astype(str)  # Convert numeric values to string
z_text = z_text.values  # Get the numpy array format

# Create an annotated heatmap
heat_map_plotly = ff.create_annotated_heatmap(
    z=corr_metrics.values,  # Correlation values
    x=list(corr_metrics.columns),  # x-axis labels
    y=list(corr_metrics.index),  # y-axis labels
    colorscale='Agsunset',  # Color scale
    annotation_text=z_text,  # Use the rounded numeric text as annotation
    showscale=True,  # Show the color scale
    font_colors=['black', 'white'],  # Font colors for annotations background
    textfont=dict(size=10)  # Font size of the annotation text
)

layout = go.Layout(title="Beer Quality Correlation Factor",  # Title of the heatmap
                   xaxis=dict(title='Metrics'),  # X-axis label
                   yaxis=dict(title='Metrics'))  # Y-axis label

# Create a Figure
fig = go.Figure(data=heat_map_plotly.data, layout=layout)

# Show the correlation heatmap
fig.show()
