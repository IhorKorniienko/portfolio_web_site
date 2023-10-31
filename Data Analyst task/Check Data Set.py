import pandas as pd

# To Do list:
# 1.1 Obtain the data sets and read it in Pycharm
# 1.2 Explore the data
# 1.3 Clean/compute the data
# 1.4 Visualize the results

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

# used lambda to apply the computation to each row of the data frame
col = data[data.select_dtypes(['object']).columns] = \
    data.select_dtypes(['object']).apply(lambda i: i.astype('category'))

# Check columns DataFrame structure
col.info()
data.info()


# Verify if there are missing values
print("Columns with null values:")
print(data.isnull().sum())

# Verify in terms of % rate what is the values of missing data:
print("Missing data of beer alcohol by volume Rate(%):")
print(round(67785 / 1586614 * 100, 2),"%")


# Remove null Values from the data sets
remove_nulls = data.dropna()
remove_nulls.info()

# Check columns if any null values exist
print("Check if any null values in all columns:")
print(remove_nulls.isnull().sum())

# After the verification we identified that we have a blended data set with text converted as 'category'
# and which columns possess actual values (int)
