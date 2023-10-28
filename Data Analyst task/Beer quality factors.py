import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly as py

# read the file:
data = pd.read_csv('beer_reviews.csv', low_memory=False)

corr_metrics = data.corr()

heat_map_plotly = ff.create_annotated_heatmap(
    z=corr_metrics.values,
    x=list(corr_metrics.columns),
    y=list(corr_metrics.index),
    colorscale='Agsunset',
    annotation_text=corr_metrics.round(2).values,
    showscale=True,
    font_colors=['snow'])

layout = go.Layout(title="Beer quality correlation factor")

fig = go.Figure(data=heat_map_plotly, layout=layout)

# show the correlation that impacts the quality
py.offline.iplot(fig)
