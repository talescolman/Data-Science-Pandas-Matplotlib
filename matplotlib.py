import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

x_axs = np.array([3, 26]) # x-axis (can be any number of values as long as the y-axis follow the same quantity)
y_axs = np.arrays([1,40]) # y-axis (if you left it out, MatPlotlib will fill it automatically with 0, 1, 2, 3 etc)

plt.plot(x_axs, y_axs) # will create your graphic
plt.grid() # add grid lines to the plot plt.grid(axis = 'x') will only display the 'x-axis' gridlines
plt.show() # will print your graphic after its creation

# Labels
plt.title("My Graph", fontdict = font1, loc = 'right') # this creates a title for the image. loc = align
plt.xlabel("Days", fontdict = font2) # fontdict = different font styles
plt.ylabel("Budget", fontdict = font2)


# You can use MARKERS to change the style of your line
plt.plot(x_axs, y_axs, marker = 'o') # this will print an O on your values
plt.plot(x_axs, y_axs, marker= 'p') # this will print a small pentagonon on your values
plt.plot(x_axs, y_axs, marker= 'h', ms = 13) # this will print an hexagon of the size 17 on your values 
plt.plot(x_axs, y_axs, marker = 'h', ms = 13, mec = 'y') # mec means the edge color of your marker, Yellow in this example.
plt.plot(x_axs, y_axs, marker = 'h', ms = 13, mfc = 'y') # mfc means the inside color of your marker, Yellow in this example.

# Make sure to read the whole list of markers on the official documentation
# When taling about colors, Hexadecimal values can be used.

plt.plot(x_axs, y_axs, ls = '--') # change the line style to -- (dasehd line)
plt.plot(x_axs, y_axs, c = 'r') # change the color of the line to red
plt.plot(x_axs, y_axs, lw = '18.5') # change the width of the line to 18.5 (always a float number)
plt.grid(c = 'b', ls = '--', lw = '0.5') # you can also format the gridlines

# fmt (Format Strings) 'marker line color'
plt.plot(x_axs, y_axs, 'p:b') # colors can be red(r),green(g),blue(b),yellow(y),black(k) and white(w)
plt.plot(x_axs, y_axs, 'h--y') # the -- means a dashed line. Your line can be '-'' (solid line), ':'' (dotted line) '-.'' (dashed/dotted line) and '--'' (dashed line)

# plot multiple lines
plt.plot(x_axs)
plt.plot(y_axs)
plt.show()

# plot multiple figures using subplot()

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) # 1 row, 2 columns, first plot
plt.plot(x,y)
plt.title("First plot") # title of the first plot

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2) # 1 row, 2 columns, second plot
plt.plot(x,y)
plt.title("Second plot")

plt.suptitle("My example:") # this will add a single title to the whole image
plt.show()

# example of 6 plots
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show() 

# scatter()

x = np.array([4,7,12,7,6])
y = np.array([102,94,14,245,195])

plt.scatter(x, y)
plt.show()

# We usually plot two different scatter() to compare them

x = np.array([4,7,12,7,6])
y = np.array([102,94,14,145,195])
plt.scatter(x, y, color = '#88c999')

x = np.array([1,2,7,12,7])
y = np.array([105,94,16,135,99])
plt.scatter(x, y, color = 'blue')

plt.show()

# Change the size of the markers
x = np.array([4,7,12,7,6])
y = np.array([102,94,14,145,195])
sizes = np.array([10,20,55,14,8])
plt.scatter(x, y, s=sizes, alpha=0.5) # alpha will change the transparency of the markers

plt.show()

# ColorMap
x = np.array([4,7,12,7,6])
y = np.array([102,94,14,145,195])
colors = np.array([0,10,20,30,40]) # create a color array 
plt.scatter(x, y, c=colors, cmap='seismic') # search the official documentation for all the different colormap styles 

plt.colorbar() # this will print the bar on your image

plt.show()

# bar()

x = np.array(["First", "Second", "Third"])
y = np.array([8, 7, 4])

plt.bar(x,y, color = "yellow", width = 0.5) #plt.barh(x,y, height = 0.5) to show horizontal bars
plt.show()

#hist()

x = np.random.normal(125, 8, 247)

plt.hist(x)
plt.show()

# pie()
y = np.array([15, 35, 35, 15])
ylabels = ["VW", "FORD", "BMW", "VOLVO"]
yexplode = [0, 0.2, 0, 0]
ycolors = ["blue", "red", "yellow", "grey"]

plt.pie(y, labels = ylabels, startangle = 90, explode = yexplode, shadow = True, colors = ycolors) # standard startangle is 0, explode is to detach some part
plt.legend()
plt.show()