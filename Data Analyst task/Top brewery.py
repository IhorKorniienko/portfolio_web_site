import pandas as pd
import plotly.graph_objects as go
import plotly as py

data = pd.read_csv('beer_reviews.csv', low_memory=False)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Verify Top 5 beers with the strongest alcohol by volume:
data = data[['brewery_name', 'beer_name', 'beer_abv']]. \
    sort_values('beer_abv', ascending=False). \
    drop_duplicates('brewery_name').head(5).sort_values('beer_abv', ascending=True)
print(data)

# Visualize the outcome, plot bar chart:
bar = [go.Bar(x=data['beer_abv'] / 100,
              y=data['brewery_name'],
              text=data['beer_name'],
              hoverinfo='x',
              orientation='h',
              textposition='inside',
              opacity=0.7)]

# choose layout:
layout = go.Layout(title='Top 5 beers with the strongest alcohol by volume', title_x=0.5,
                   xaxis=dict(title='Alcohol By Volume',
                              tickformat='.2%'),
                   margin=dict(r=500),
                   font=dict(family='Times New Roman',
                             color='darkblue'))

view = go.Figure(data=bar, layout=layout)
view.update_traces(marker=dict(color='green'))

# remove gridlines for nicer view
view.update_layout(xaxis=dict(showgrid=False, showline=True, linewidth=2, linecolor='black'),
                   yaxis=dict(showline=True, linewidth=2, linecolor='black'))

py.offline.iplot(view)

# According to the executed analysis the strongest beer is produced by 'Schorschbrau' with the highest rate: 57.7% abv
