import folium
import pandas as pd
import json
from folium import plugins

#read the data
df = pd.read_excel('January+2021+Data+Tables+SD+Food+Insecurity.xlsx', sheet_name='FoodAssistJan2021Zip')

#read the san diego boundary data
with open('Zip Codes.geojson') as f:
    sdArea = json.load(f)

#group the food insecure dataframe by zip code
numFoodInsecuritySeries = [df['Zip Code'], df['Total Food Assistance']]

#initialize an empty dataframe to store this new data
numFoodSecurityByZip = pd.DataFrame()
#populate the new dataframe with a 'zipcode' column and a 'numFoodInsecure' column
numFoodSecurityByZip['zipcode'] = [str(i) for i in numFoodInsecuritySeries[0]]
numFoodSecurityByZip['numFoodInsecure'] = [int(i) for i in numFoodInsecuritySeries[1]]
numFoodSecurityByZip.drop(numFoodSecurityByZip.tail(1).index,inplace=True) 

#initialize the LA County map
sdMap = folium.Map(location=[32.7157,-117.1611], zoom_start=12)

#draw the choropleth map. These are the key components:
#--geo_path: the geojson which you want to draw on the map [in our case it is the zipcodes in LA County]

#--data: the pandas dataframe which contains the zipcode information 
# AND the values of the variable you want to plot on the choropleth

#--columns: the columns from the dataframe that you want to use 
#[this should include a geospatial column [zipcode] and a variable [numFoodInsecure]

#--key_on: the common key between one of your columns and an attribute in the geojson. 
#This is how python knows which dataframe row matches up to which zipcode in the geojson

folium.Choropleth(geo_data='Zip Codes.geojson', data=numFoodSecurityByZip, columns=['zipcode', 'numFoodInsecure'],
                 key_on='feature.properties.zip', fill_color='YlGn', fill_opacity=1)

sdMap.save('sdChoropleth.html')
