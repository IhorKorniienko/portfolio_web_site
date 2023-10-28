import pandas as pd

# read the file:
data = pd.read_csv('beer_reviews.csv', low_memory=False)

# set a default number of rows and check names of the columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(f'Number of rows & columns: {data.shape}')
print(data.head(10))

# check data types and convert 'object' to 'category'
col = data[data.select_dtypes(['object']).columns] = \
        data.select_dtypes(['object']).apply(lambda i: i.astype('category'))

# Check columns DataFrame structure
col.info()
data.info()

# After the verification we identified that we have a blended data set with text converted as 'category'
# and which columns possess actual values (int)
