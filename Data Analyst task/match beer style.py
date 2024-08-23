import pandas as pd
import plotly.graph_objects as go
import plotly as py

# Read the file:
data = pd.read_csv('beer_reviews.csv', low_memory=False)

# Aggregate count & mean for relevant variables
aro_appear = data[['beer_style', 'review_aroma', 'review_appearance', 'review_overall']] \
    .pivot_table(index="beer_style", aggfunc=('count', 'mean'))

# Flatten pivot table
aro_appear.columns = aro_appear.columns.to_series().str.join('_')
aro_appear.reset_index(inplace=True)

# Remove redundant '_count' columns
aro_appear.drop(list(aro_appear.filter(regex='count')),
                axis=1,
                inplace=True)

# Add average of combined aroma and appearance
aro_appear['aroma_appear_mean'] = (aro_appear['review_appearance_mean'] +
                                   aro_appear['review_aroma_mean']) / 2

# Add absolute average distance from mean
aro_appear['diff_from_mean'] = abs(aro_appear['review_appearance_mean'] - aro_appear['review_aroma_mean'])

# Sort for plotly
sort_aro_appear = aro_appear.sort_values('aroma_appear_mean', ascending=False) \
    .head(10) \
    .sort_values('aroma_appear_mean', ascending=True)

# Aroma-Appearance Dumbbell Plot Workaround
p1 = go.Scatter(
    x=sort_aro_appear['aroma_appear_mean'],
    y=sort_aro_appear['beer_style'],
    error_x=dict(
        type='data',
        array=sort_aro_appear['diff_from_mean'] / 2,
        thickness=1.5),
    mode='markers',
    name='Combined Average',
    marker=dict(
        color='rgba(84, 110, 122, 0.95)',
        line=dict(
            color='rgba(84, 110, 122, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=8
    )
)

# Aroma Rating Dot Plot
p2 = go.Scatter(
    x=sort_aro_appear['review_aroma_mean'],
    y=sort_aro_appear['beer_style'],
    mode='markers',
    name='Aroma Average',
    marker=dict(
        color='rgba(229, 57, 53, 0.95)',
        line=dict(
            color='rgba(229, 57, 53, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=8
    )
)

# Appearance Rating Dot Plot
p3 = go.Scatter(
    x=sort_aro_appear['review_appearance_mean'],
    y=sort_aro_appear['beer_style'],
    mode='markers',
    name='Appearance Average',
    marker=dict(
        color='rgb(1, 87, 155, 0.95)',
        line=dict(
            color='rgba(1, 87, 155, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=8
    )
)

# Set layout
layout = dict(
    title='Top 10 Beer Styles by Combined Appearance/Aroma Average',
    xaxis=dict(
        showline=True,
        showticklabels=True,
        ticks='outside',
        title='Rating',
        hoverformat='.2f',
        autorange=True,
        showgrid=False),
    margin=dict(l=250),
    font=dict(family='Courier New, monospace', color='dark gray'),
    legend=dict(
        font=dict(
            size=10,
        ),
        yanchor='bottom',
        xanchor='right',
    ),
    hovermode='closest'
)

# Plot it
fig = go.Figure(data=[p1, p2, p3], layout=layout)
# Use plot instead of iplot to open in a web browser
py.offline.plot(fig, filename='beer_style_plot.html', auto_open=True)
