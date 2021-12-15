import pandas as pd
data = pd.read_csv('artwork_sample.csv')
#sets a variable and read artwork_sample.csv file

print(data.head())
#prints the first five rows
print(data.dtypes)
#prints the data types 


fulldf = pd.read_csv('artwork_data.csv', low_memory=False)
#sets a variable and reads artwork_data.csv file
pd.to_numeric(fulldf.height, errors= "coerce")
#uses panda's to_numeric to change data type
fulldf.height = pd.to_numeric(fulldf.height, errors = "coerce")


#different ways to aggregate data on year column
#aggregate is the process of gathering data and presenting it in a summarized format
print(data.year.min())
print(data.year.max())
print(data.year.sum())
print(data.year.mean())
print(data.year.std())

#using agg (aka aggregate) function allows us to aggregrate several functions at once. 
print(data.year.agg(['min', 'max', 'mean', 'std']))

# #by using axis you can aggregrate columns
# print(data.agg('mean', axis="columns"))

#normalization is adjusting values/scale in the columns 

#first way to normalize data
height = data.height
normalization =(height - height.mean())/ height.std()
print(normalization)

#second way to normaliza data
minmax= (height - height.min())/(height.max() - height.min())
print(minmax.min())
print(minmax.max())

#sets the original height column to the normalized values
data.height = minmax
#creates new column with standardized height values
data['standardized_height'] = normalization

data.height.transform(lambda x: print(x))

#counts the number of unique items by row and column
print(data.groupby('artist').transform('nunique'))
print(data.groupby('artist')['height'].transform('mean'))

#assigns data to new column on dataframe
data['mean_height_by_artist'] = data.groupby('artist')['height'].transform('mean')

#filter allows you to limit what columns you see
print(data.filter(items=["id", "artist"]))
#filters data but is case sensitive ex. lowercase, uppercase
print(data.filter(like="year"))
#prints case insenstive = anything with year
print(data.filter(regex="(?i)year"))
#drop rows by index name
print(data.drop(0))
#drop multiple rows by using labels
print(data.drop(labels=[0, 1, 2]))
#drop columns by name and adding axis
print(data.drop('id', axis=1))
#another way to drop columns or multiple columns
print(data.drop(columns=['height', 'width', 'depth']))

#none of the previous drops change the original data frame.
#in order to make the drop changes permanent you must specify inplace=True
print(data.drop(columns=['id'], inplace=True))
print(data)

#A more effective way of doing this is at inital import of file. 
# Only import what you need.
# data = pd.read_csv("artwork_sample.csv", usecols=['artist', 'title'])
print(data)

#makes everything lowercase
print(data.columns.str.lower())

data = pd.read_csv("artwork_sample.csv")
# import re

# #makes our column names that are camelCase to snake_case
# #allows for a more uniform and tidy dataset
# data.columns = [re.sub(r'([A-Z])', r'_\l', x).lower() for x in data.columns]
# print(data.columns)

#one way to rename 
data.rename(columns={"thumbnailUrl" : "thumbnail"})
#another way to rename that applies it to columns instead of rows
data.rename({'thumbnailUrl' : 'thumbnail'}, axis=1)

