#page 287-, subject involing: MATPLOTLIB,  IMPORT DATA, DATETIME
#these are all side notes, all the way pushed to the lefthand wall
    #these are sub-excise topics
        #these are categorical topics to keep me focused. W/o further due, I shall begin 

        #27. matplotlib
    #line plot 
import matplotlib.pyplot as plt
#as plt, saves me from entering pyplot everytime 
input_value=[1,2,3,4,5]
squares=[1,4,9,16,25]
#get the x, y varaibles defined 
plt.plot(input_value,squares,linewidth=5)
plt.title("Square Adjusted Line Plot Example")
plt.xlabel("Input Value",fontsize=12)
plt.ylabel("Squared Input Value",fontsize=12)
#make it readible 
plt.tick_params(axis='both',labelsize=14)

#before enterng to the next topic, scatter, make sure to save individually, 
#other wise, 2 graphs appears at one. I am just lazy here

    #scatter plot a dot: plt.scatter(x,y,s=size)
import matplotlib.pyplot as plt
plt.scatter(5,10, s=200)

plt.title("Scatter Plot Example",fontsize=24)
plt.xlabel("X-axis",fontsize=12)
plt.ylabel("Y-axis",fontsize=12)
plt.tick_params(axis='both',labelsize=14)

plt.show()

    #scatter plot a serie of dots: plt.scatter(x_value, y_value, s=size)
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)

plt.title("Scatter Plot Example",fontsize=24)
plt.xlabel("X-axis",fontsize=12)
plt.ylabel("Y-axis",fontsize=12)
plt.tick_params(axis='both',labelsize=14)

plt.show()

    #auto-calculation, line 
import matplotlib.pyplot as plt
x_values=list(range(1,1001))
#this part make sure it is list(range()) instead of list[range()]
y_values=[x**2 for x in x_values]
#**2 is ^2
#now have defined x in x_values as x^2
plt.scatter(x_values, y_values, s=40)
plt.title("Auto Scatter Plot Example",fontsize=24)
plt.xlabel("X-axis",fontsize=12)
plt.ylabel("Y-axis",fontsize=12)
plt.axis([0,1100,0,110000])
#here is the range fo the x and y axis 
plt.show()

    #changing colors 
import matplotlib.pyplot as plt
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)

plt.title("Auto Scatter Plot Colored Example",fontsize=24)
plt.xlabel("X-axis",fontsize=12)
plt.ylabel("Y-axis",fontsize=12)
plt.axis([0,1100,0,110000])

plt.show()
#for more reference of coloring, visit:http://matpotlib.org/
#under example--color examples--colormaps_reference 

        #28. Pygal 
#####problematic 


        #29 import data
import csv 
filename='sitka_weather_07-2014.csv'
with open(filename) as f: 
# to save filename which is the weather.csv to as f 
    reader=csv.reader(f)
    #use reader function to read it in csv format 
    header_row=next(reader)
    #store every first line in header_row 
    print(header_row)
    #make sure you place the weather data in the same doc where this py file is at
    #now you get the title line of the weather data, seperated by, in a line 

    #if we want to list the titles in a vertical presentation 
import csv
filename='sitka_weather_07-2014.csv'
with open(filename) as f: 
    reader=csv.reader(f)
    header_row=next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #extract max temperature 
filename='sitka_weather_07-2014.csv'
with open(filename) as f: 
    reader=csv.reader(f)
    header_row=next(reader)
    #step 1: create an empty list for max tem to be stored in 
    highs=[]
    for row in reader: 
    #step 2: go look for row in reader at row[0] b/c that through index, we know (1,'Max TemperautreF')
        highs.append(row[1])
        #step 3: compile the list
    print(highs)

    #now convert the temp into integers 
filename='sitka_weather_07-2014.csv'
with open(filename) as f: 
    reader=csv.reader(f)
    header_row=next(reader)
    
    highs=[]
    for row in reader:  
        high=int(row[1])
        #high is every row one and converted into integers
        highs.append(high)
        #compile all high
    print(highs)

    #graph the max temperature 
#step 1: prep, get all tools out and setup
import csv
from matplotlib import pyplot as plt

#step 2: which file, where to read 
filename='sitka_weather_07-2014.csv'
with open(filename) as f: 
    reader=csv.reader(f)
    header_row=next(reader)

#step 3: which particular quality to graph, in this case, max temp []
    highs=[]
    for row in reader: 
        high=int(row[1])
        highs.append(high)

#step 4: set up the graph dimension 
plt.plot(highs,c='red')
plt.title("Daily Max Temperature/July 2014",fontsize=24)
plt.xlabel("Day",fontsize=14)
plt.ylabel("Temp in F",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

        #30. datetime 
import csv
from datetime import datetime 
from matplotlib import pyplot as plt 

filename='sitka_weather_07-2014.csv'
with open(filename) as f: 
    reader=csv.reader(f)
    header_row=next(reader)

dates, highs=[],[]
for row in reader: 
    current_date=datetime.strptime(row[0],"%Y-%m-%d")
    #strptime helps to read date to formatted"%Y-etc-etc
    dates.append(current_date)

