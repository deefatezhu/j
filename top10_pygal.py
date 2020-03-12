#In this excercise I would like to explore the top10 most commonly used*defined by myself... Pygal examples 
#when in doubt, go visit: http://www.pygal.org   
       
        #1. Bar Chart 
import pygal
height=[0,3,5,7,10]
bar=pygal.Bar()
#this tells pygal to set a Bar(Cap) chart for our bar 
bar.title='Bar Chart'
bar.x_labels=['1','2','3','4','5']
#x cords 
bar.x_title='Cat'
bar.y_title='Height of Cats'
bar.add('H',height)
#this officially sets the y variable and its name "h"
bar.render_to_file('pygal_bar_chart.svg')

        #2. Barss Chart 
import pygal
height_1=[1,3,5,7,10]
bar=pygal.Bar()
height_2=[15,7,8,10,20]
bar.title='Barss Chart'
#notice, the x_labels I have omitted 
#it is optional if it's just 1,2,3,4
bar.y_title="height of Cats vs Dog"
bar.add('C',height_1)
bar.add('D',height_2)
bar.render_to_file('pygal_barss_chart.svg')

#another simple way doing bar chart 
import pygal 
bar=pygal.Bar(print_values=True, value_formatter=lambda x: '{}'.format(x))
#adding formatter, so we see assigned x on chart
bar.title='My Cats Weight'
bar.x_labels=map(str, range(2015,2020))
bar.add('Tom',[1,3,5,7,10], formatter=lambda x: '<%s>' % x)
bar.add('Jerry',[15,7,8,10,20])
bar.render_to_file('pygal_barss_chart2.svg')

#emphasising on a one particular bar or bars 
bar=pygal.Bar()
bar.add('Serie',[{'value':2},3,4,{'value':10,'color':'red'},{'value':11,'color':'red'},3,4])
bar.render_to_file("pygal_colored_bar.svg")

        #3. Stacked Bar 
bar=pygal.StackedBar()
#notice spelling here... StackedBar 
bar.add('Cat Height in Q1',[3,3,4,3,4])
bar.add('Cat Height added in Q2',[1,2,1,2,1])
bar.render_to_file('pygal_stacked_bar.svg')
##??? COME BACK AND FIX THE SPACING HERE, FUCKING UGLY 

        #4. Horizontal Bar 
bar=pygal.HorizontalBar()
bar.title="Grocery Items I Buy the Most (in%)"
bar.add('Water',20)
bar.add('Eggs',20)
bar.add('Milk',10)
bar.add('Lemon',5)
bar.add('Cabbage',15)
bar.add('Tofu',10)
bar.add('others',20)
bar.render_to_file('pygal_horizontal_bar.svg')

        #5. Line Graph 
line=pygal.Line()
line.title="How Often My heart Skipps A Beat"
line.x_labels=map(str,range(2012,2020))
line.add('Love Related',[3,3,4,1,1,1,2,1])
line.add('School Related',[0,0,5,4,3,2,4,1])
line.add('Social Related',[None,None,None,None,1,1,1,1])
#none (skipped) and 0 are two different things on the graph
line.add('Others',[2,3,1,2,3,4,1,5])
line.render_to_file('pygal_line.svg')

        #6. Histogram
#Histogram(takes cords) vs Bar chart (a formatted stick with gap)
histo=pygal.Histogram()
histo.add('Wide bars',[(5,0,10),(4,5,4)])
histo.add('Narrow bars',[(1,0,1),(10,1,2)])
histo.render_to_file('pygal_histogram.svg')

        #7. Pie (%)
pie=pygal.Pie()
pie.title="My B Sides"
pie.add('Feimusic',20)
pie.add('dating',20)
pie.add('Naybr',15)
pie.add('reading',15)
pie.add('partying/hang out',20)
pie.add('family',10)
pie.render_to_file('pygal_pie.svg')

#donut.. 
pie=pygal.Pie(inner_radius=4)

#ring...
pie=pygal.Pie(inner_radius=.75)

#half pie...
pie=pygal.Pie(half_pie=True)

        #8. Radar
#I don't think I will ever use it but it looks cool 
radar=pygal.Radar()
radar.title="Judy's Skillsets 2012-2020"
radar.x_labels=['Artisic','Communication','Learninging Ability','Attractiveness','Robustness','Analytical Skills']
radar.add('Me in 2012',[40,30,80,50,20,30])
radar.add('Me in 2015',[50,75, 75,80,70,60])
radar.add('Me in 2018',[60,80,80,80,76,80])
radar.add('Me in 2020',[80,85,85,85,80,80])
radar.render_to_file('pygal_radar.svg')

        #9. XY for correlation 
from pygal.style import NeonStyle
xy=pygal.XY(stroke=False, style=NeonStyle)
xy.title="Various' Food and Judy's Happiness"
xy.add('Tofu',[(1,2),(5,6),(9,10),(3,4)])
xy.add('Chocolate',[(2,1),(1,9),(2,8),(3,5)])
xy.add('Coffee',[(2,2),(5,5),(9,9)])
xy.add('Correlation',[(0,0),(10,10)],stroke=True)
#this adds the line, (0,0) to (10,10)
xy.render_to_file('pygal_xy.svg')

        #10. Styling 
#coloring (defult) aka white paper 
from pygal.style import DefaultStyle
chart=pygal.StackedLine(fill=True, interpolate='cubic',sytle=DefaultStyle)
chart.add('A', [1, 3,  5, 16, 13, 3,  7])
chart.add('B', [5, 2,  3,  2,  5, 7, 17])
chart.add('C', [6, 10, 9,  7,  3, 1,  0])
chart.add('D', [2,  3, 5,  9, 12, 9,  5])
chart.add('E', [7,  4, 2,  1,  2, 10, 0])
chart.render_to_file('pygal_default_styling.svg')

#coloring (neon) aka neon lights on a dark paper 
from pygal.style import NeonStyle
chart = pygal.StackedLine(fill=True, interpolate='cubic', style=NeonStyle)

#coloring (light) aka excel vibe  

#coloring (light solarized) aka warm rainbow   

#coloring (clean) aka less offended default vers.

#coloring (red blue) aka pastel ish 
from pygal.style import RedBlueStyle
chart=pygal.StackedLine(fill=True, interpolate='cubic',sytle=RedBlueStyle)

#coloring (light green) aka spring green 
from pygal.style import LightGreenStyle
chart=pygal.StackedLine(fill=True, interpolate='cubic',style=LightGreenStyle)

#coloring (blue) aka ocean sunny blue 