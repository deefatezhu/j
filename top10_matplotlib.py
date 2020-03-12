#In this excercise I would like to explore the top10 most commonly used*defined by myself... Matplotlib examples
#when in doubt, visit: https://matplotlib.org/gallery/index.html     
      
        #1. Line Plot  
import matplotlib.pyplot as plt
input_value=[1,2,3,4,5]
squares=[1,4,9,16,25]
#get the x, y varaibles defined 
plt.plot(input_value,squares,linewidth=5)
plt.title("Square Adjusted Line Plot Example")
plt.xlabel("Input Value",fontsize=12)
plt.ylabel("Squared Input Value",fontsize=12)
#make it readible 
plt.tick_params(axis='both',labelsize=14)
plt.show()

        #2. Grouped Bar Chart 
import numpy as np 
import matplotlib.pyplot as plt

labels=['Q1','Q2','Q3','Q4']
men_means=[20,35,30,30]
women_means=[25,32,34,20]
men_std=[2,3,4,1]
women_std=[3,5,2,3]
width=0.35 
#width refering to the width of the bar chart

fig,ax=plt.subplots()
ax.bar(labels,men_means,width,yerr=men_std,label='Men')
#this says, x=labels, y=men_means, of bar size 0.35, with yerror=men_std, label it 'Men'
ax.bar(labels,women_means,width, yerr=women_std,bottom=men_means,label='Women')
#similar, bottom means, women_means is on top of men_means
ax.set_ylabel('Scores')
ax.set_title("scores by group and gender")
ax.legend()
#ax.legend shows the men/women of which color on the side 
plt.show()

        #3. Horizontal Bar Chart 
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
#arange not arrange, stands similar to range function 
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  
# labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()

      
        #4. Simple plot
import matplotlib.pyplot as plt
import numpy as np

#data for plotting 
t=np.arange(0.0,2.0,0.01)
#arange not arrange, stands similar to range function 
# >>> np.arange(3)
# array([0, 1, 2])
# >>> np.arange(3.0)
# array([ 0.,  1.,  2.])
# >>> np.arange(3,7)
# array([3, 4, 5, 6])
# >>> np.arange(3,7,2)
# array([3, 5])
s=1+np.sin(2*np.pi*t)

fig,ax=plt.subplots()
ax.plot(t,s)

ax.set(xlabel='time(s)',ylabel='voltage(mV',title='About as simpoe as it gets')
ax.grid()

plt.show()

        #5. Animated Line Plot  
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,


def animate(i):
    line.set_ydata(np.sin(x + i / 100))  # update the data.
    return line,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)

plt.show()
# To save the animation, use e.g.--ani.save("movie.mp4")


       
        #6. Pie Chart 
#basic
import matplotlib.pyplot as plt
labels='Tofu','Eggs','Water','Others'
#will be counterclockwise in the pie
sizes=[15,30,45,10]
explode=(0,0.1,0,0)
#explode the second pie, which is the Eggs, will be standing alone
fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
ax1.set_title('Most Bought Grocery')
#equal ensures the pie is drawn as a circle 
plt.show()


