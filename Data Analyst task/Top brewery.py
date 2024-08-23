import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

# Load the data
data = pd.read_csv('beer_reviews.csv', low_memory=False)

# Set display options for pandas DataFrame
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Verify Top 5 beers with the strongest alcohol by volume:
top_beers = data[['brewery_name', 'beer_name', 'beer_abv']]. \
    sort_values('beer_abv', ascending=False). \
    drop_duplicates('brewery_name').head(5).sort_values('beer_abv', ascending=True)
print(top_beers)

# Visualize the outcome, plot bar chart:
bar = [go.Bar(x=top_beers['beer_abv'],  # Use beer_abv directly
              y=top_beers['brewery_name'],
              text=top_beers['beer_name'],
              hoverinfo='text',  # Changed to 'text' to show beer name on hover
              orientation='h',
              textposition='inside',
              opacity=0.7)]

# Choose layout:
layout = go.Layout(title='Top 5 Beers with the Strongest Alcohol by Volume', title_x=0.5,
                   xaxis=dict(title='Alcohol By Volume (%)'),  # Updated title
                   margin=dict(r=500),
                   font=dict(family='Times New Roman', color='darkblue'))

# Create figure
view = go.Figure(data=bar, layout=layout)
view.update_traces(marker=dict(color='green'))

# Remove gridlines for nicer view
view.update_layout(xaxis=dict(showgrid=False, showline=True, linewidth=2, linecolor='black'),
                   yaxis=dict(showline=True, linewidth=2, linecolor='black'))

# Display the plot in a browser
pyo.plot(view, filename='beer_reviews.html', auto_open=True)

# Information about the strongest beer
strongest_beer = top_beers.iloc[-1]  # Last entry after sorting is the strongest
print(f"The strongest beer is produced by '{strongest_beer['brewery_name']}' with the highest rate: {strongest_beer['beer_abv']}% abv")
