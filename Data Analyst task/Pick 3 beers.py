import pandas as pd
import plotly.graph_objects as go
import plotly as py
import seaborn as sns

# read the file:
data = pd.read_csv('beer_reviews.csv', low_memory=False)

# set a default number of rows and check names of the columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# verify the ranking of beers that are most popular based on the overall views of people. Calc average:
# data_set = pd.pivot_table(data=data, index='beer_name', values='review_overall',
#                           aggfunc=('count', 'mean')).dropna().round(2)

data_set = data[['beer_name', 'review_overall']]. \
    pivot_table(index="beer_name", aggfunc=('count', 'mean')).dropna().round(2)

# Make pivot headers much more readable
data_set.columns = data_set.columns.to_series().str.join('_')
data_set.reset_index(inplace=True)

# Sort data from the highest review_overall rates:
data_set = data_set.query('review_overall_count >= 1000').sort_values('review_overall_mean', ascending=False).head(35)

print(data_set)

# plotting visuals
# .as_hex returns the hexadecimal representation of the color
set_colors = sns.color_palette('husl', n_colors=len(data_set['beer_name'])).as_hex()

bar = [go.Bar(x=data_set['beer_name'],
              y=data_set['review_overall_mean'] / 100,
              text=data_set['review_overall_mean'] / 100,
              hoverinfo='y, x',
              textposition='outside',
              texttemplate='%{text: .2%}',
              opacity=0.8,
              marker=dict(color=set_colors))]

# choose layout:
layout = go.Layout(title='The beers that I recommend to the people', title_x=0.5,
                   xaxis=dict(title='Top Beer Names'),
                   yaxis=dict(tickformat='.2%', title='Overall opinion of the people (average rate %)'),
                   margin=dict(r=50),
                   font=dict(family='Times New Roman',
                             color='Black'))

view = go.Figure(data=bar, layout=layout)
view.update_layout(xaxis=dict(showline=True, linewidth=2, linecolor='black', showgrid=False),
                   yaxis=dict(showline=True, linewidth=2, linecolor='black'))
# py.offline.iplot(view)
view.show()

# I would suggest to pick up beers based on overall opinion ratings coming from the data sets.
# in this case these are the famous brands:
# 1.1 Trappist Westvleteren 12
# 1.2 Pliny The Elder
# 1.3 Weihenstephaner Hefeweissbier
