import pandas as pd
import matplotlib.pyplot as plt # I also did a Matplotlib tutorial

df = pd.read_csv('my_cars.csv')

df.plot()

plt.show() 

# rank plot
df.plot(x="Car Brand", y=["Model", "HP", "Price", "Year"])
plt.show()

# scatter plot

df.plot(kind = 'scatter', x = 'Model', y = 'HP')
plt.show()

# historogram plot

df["HP"].plot(kind = 'hist')
plt.show()

# list of kind = "" values 
# "area"
# "box" 
# "density" or "kde"
# "hexbin"
# "line"
# "pie"
# "bar" (vertical bar charts)
# "barh" (horizontal bar charts.)



