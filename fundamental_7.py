#page 324-, subject involing: Import JSON, PYGAL-LINECHART, 
#these are all side notes, all the way pushed to the lefthand wall
    #these are sub-excise topics
        #these are categorical topics to keep me focused. W/o further due, I shall begin 

        #31. Import JSON 
import json
filename='btc_close_2017.json'
with open(filename) as f: 
    btc_data=json.load(f)
#now the btc_data is ready to be read 
for btc_dict in btc_data: 
    date=btc_dict['date']
    month=btc_dict['month']
    week=btc_dict['week']
    weekday=btc_dict['weekday']
    close=btc_dict['close']
    print("{} month {} week{},{}, the close price is {} rmb".format(date, month,week, weekday, close))
#now we are going through every defined variable and printing them by each date. 

    #the numbers are not in the right format 
#we need to convert close=btc_dict['close'] to integers
import json
filename='btc_close_2017.json'
with open(filename) as f: 
    btc_data=json.load(f)

for btc_dict in btc_data: 
    date=btc_dict['date']
    month=btc_dict['month']
    week=btc_dict['week']
    weekday=btc_dict['weekday']
    close=int(float(btc_dict['close']))
    #now close in the btc_dic is integers 
    print("{} month {} week{},{}, the close price is {} rmb".format(date, month,week, weekday, close))

        #32. use pygal to make a line chart  
#step 1: making empty lists 
dates=[]
months=[]
weeks=[]
weekdays=[]
close=[]

#step 2: get each day's data compiled into each list 
for btc_dict in btc_data: 
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close']))
#step 3: now we have the x variable: dates 
#y variable: btc price 
#however, dates(365) may look too crowded so we need pygal to beautify 

#step 4: pygal 
import pygal 
line_chart=pygal.line(x_label_rotation=20,show_minor_x_labels=False)
#x_label_rotation= x_label: rotate by 20 degree, avoid crowdiness
#show_minor_x_labels=False: no need to show ALL x 
line_chart.title='Closing Price/2017'
line_chart.x_label='Dates'

N=20 
line_chart.x_label_major=dates[::N]
#this means x shows up every 20 unit(day)

line_chart.add("closing price",close)
#I suppose, this .add is the y variable: 'closing price'taken from the y, which is the close list 
line_chart.render_to_file('BTC Closing Price 2017.svg')
#render saves the line chart 

        #33. Using API

