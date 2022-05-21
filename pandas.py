import pandas as pd
import re 

# loading

df = pd.read_csv('my_file.csv') 

# reading each column

print(df[[,'Name','Age','Weight']])

# reading only the names
print(df.Name)

# sorting data by priority (age and then weight)

df.sort_values('2','3')

# adding columns into a new column

df['Total'] = df['Age'] + ['Weight'] # you can use df.iloc to add multiple columns

# filtering data

filtered_df = df.loc[(df['Name'] == 'Tom')
filtered_df.reset_index(drop=True, inplace=True) # Modify the DataFrame in place
filtered_df

# Regex

df.loc[df['Name'].str.contains('tom|john', flags=re.I, regex=True)]

# change data based on conditions

df.loc[df['Name'] == 'Tom', 'Name'] = 'Tomas'

# saving data in CSV (with ",")

df.to_csv('new_dt.csv', index=False, sep=',')
