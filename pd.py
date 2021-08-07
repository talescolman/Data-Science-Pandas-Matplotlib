import pandas as pd

# each column is a serie, and the whole table is called a DataFrame
mydataframe = {
  'brand': ["BMW", "BMW", "VW"],
  'model': ["335i", "328i", "Jetta"]
  'price': [24.500, 12.250, 8.500]
  'year': [2015, 2011, 2004]
}

# create an object with your DataFrame
myvar = pd.DataFrame(mydataframe)

print(myvar)

# you can change the index of your DataFrame
myvar = pd.DataFrame(mydataframe, index = ["car1", "car2", "car3"])

# to return a certain row
print(myvar.loc["car2"])

# you can use a dictionary as a series, this way you can index the item using its label
engines = {"bmwHP": 406, "vwHP": 123, "volvoHP": 387}

myvar = pd.Series(engines)

print(myvar)

# searching by the label
myvar = pd.Series(engines, index = ["vwHP"])

# reading CSV files
df = pd.read_csv('mydata.csv')

# in order to print the whole file, use:
print(df.to_string()) 

print(df) # will only return the first 5 rows

# reading JSON files (they work just like Python dictionaries)
df = pd.read_json('mydata.json')

# in order to print the whole file, use:
print(df.to_string()) 

print(df) # will only return the first 5 rows

print(df.head(20)) # will return the first 20 rows

print(df.tail(18)) # will return the last 20 rows

print(df.info()) # will return information about the DataFrames Object

# replace values, 3 is the row, 'vwHP' is the column, 145 is the new value
df.loc[3, 'vwHP'] = 145

# you can replace values using loops

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

# find and delete rows with duration bigger than 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True) 

# Remove rows with empty cells

new_df = df.dropna() # returns a new DataFrame, not erasing information from the original one. You can use df.dropna(inplace = True) to replace the original one

print(new_df.to_string())

# Replace rows with empty cells

df.fillna(18, inplace = True) # all empty rows will change to value 18. inplace = True is being used in order to update the orignal DataFrame and not creating a new copy. 

df["fordHP"].fillna(100, inplace = True) # will replace only the NULL values in "fordHP" column

# mean() = the average value (the sum of all values divided by number of values).

df["vwHP"].mean()

# replace all NULL values in column "vwHP" with the mean

x = df["vwHP"].mean()
df["vwHP"].fillna(x, inplace = True)  

# median() = the value in the middle, after you have sorted all values ascending.

df["vwHP"].median()

# replace all NULL values in column "vwHP" with the median

x = df["vwHP"].median()
df["vwHP"].fillna(x, inplace = True) 

# mode() = the value that appears most frequently. You can replace all NULL value in column "fordHP" following the steps above

df["fordHP"].mode()

# duplicated() is a boolean that returns TRUE if the value is duplicated

print(df.duplicated())

# removing duplicates

df.drop_duplicates(inplace = True) 

# Convert to date format 

df['Date'] = pd.to_datetime(df['Date']) # select the clumn date and format

# find correlation using corr(). 1 means one to one relation (a perfect correlation). Less than 0.6 or -0.6 is not a correlation.
df.corr() 

# HOW TO PLOT YOUR DATA IS EXPLAINED IN NOTHER TUTORIAL
