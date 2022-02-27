import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

'''
This graph is about the food Insecurity percent by different races in each month in 2020 in California
data: represent each race percent encounter food insecurity compare to the overall each race in california by month
'''
data = pd.read_csv('2022 food insecurity vs race .csv')
plt.figure(figsize=(15,8))
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#Asian Plot
plt.plot(data['Asian'],label=r'Asian',c='blue')

#white plot
plt.plot(data['white'],label=r'White',c='cyan')

#black plot
plt.plot(data['black'],label=r'Black',c='#ff8817')

#Hispanic or Latino plot
plt.plot(data['Hispanic or Latino'],label=r'Hispanic or Latino',c='#f13710')

#Other race plot
plt.plot(data['Other race'],label=r'Other race',c='#866ba8')

ind = np.arange(len(month)) 
plt.axvline(x=3,color ='black',ls =':',alpha=0.45)
plt.axvline(x=6,color ='black',ls =':',alpha=0.45)
plt.axvline(x=8,color ='black',ls =':',alpha=0.45)
plt.axhline(y=10.3,color ='red',ls =':',alpha=0.45)
plt.axhline(y=41.2,color ='red',ls =':',alpha=0.45)
plt.xticks(ind, month)
plt.legend(loc='upper right')
plt.xlabel("Month")
plt.ylabel("Percent %")
plt.title('Food Insecurity percent by races each months in 2020')
plt.ylim(5, 45)
# end for the first graph code



'''
This graph is about the average of the food insercurity in 2020 by different races
'''
name= ["Asian",'Black','Hispanic','White','Other race']
average = [data['Asian'].sum()/12,data['black'].sum()/12,data['Hispanic or Latino'].sum()/12,data['white'].sum()/12,data['Other race'].sum()/12]
plt.figure(figsize=(10,7))
plt.bar(name,average,color=['blue', 'red', 'green', 'yellow', 'cyan'])
plt.ylabel("Percent %")
plt.xlabel("Race")
plt.title('Food Insecurity percent by Races in 2020 In California')
#end for this graph


'''
This graph is the top ten population states in USA for food insecurity percent in 2020 by different races
data: each races encounter food insecurity percent in different states
'''
states= ["CA",'TX','FL','NY','PA','IL','OH','GA','NC','MI']      
California = {}
asian = [i for i in data['Asian_s'] if math.isnan(i) == False]
white = [i for i in data['white_s'] if math.isnan(i) == False]
black = [i for i in data['black_s'] if math.isnan(i) == False]
latino =[i for i in data['Hispanic_s'] if math.isnan(i) == False] 
other = [i for i in data['other_s'] if math.isnan(i) == False]

plt.figure(figsize=(10,7))
ind = np.arange(len(states)) 
width = 0.15
plt.bar(ind,asian,width,color="blue",label = 'Asian')
plt.bar(ind+width,white,width,color="red",label = 'White')
plt.bar(ind+width*2,black,width,color="green",label = 'Black')
plt.bar(ind+width*3,latino,width,color="yellow",label = 'Hispanic or Latino')
plt.bar(ind+width*4,other,width,color="cyan",label = 'Other race')
plt.xticks(ind, states)
plt.legend(loc='upper right')
plt.ylabel("Percent%")
plt.xlabel("States")
plt.title('Food Insecurity percent in each states with different races')
plt.ylim(5, 50)
plt.show()
#end for this graph
