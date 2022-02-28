import pandas as pd #For reading in data
import pgeocode #For converting zip code to longitude/latitude
import matplotlib.pyplot as plt #for plotting
import plotly.figure_factory as ff
import matplotlib.image as mpimg
import os

#Change to project directory
PROJECT_ROOT_DIR = "C:\School\ECE_143\ECE_143_Group_Project\\"

#Read in data for geographical coordinate tranformation
fname = PROJECT_ROOT_DIR + 'Data\california_foodbanks.csv'
data = pd.read_csv(fname)

#Extract zip code
#Note that some of these only get one zip code in each county may lead to more data on density
zip_codes = []
for index, row in data.iterrows():
    if row['Address'][-2:] == '\']':
        zip_codes.append(row['Address'][-7:-2])
    elif row['Address'][-5] == '-':
        zip_codes.append(row['Address'][-10:-5])
    else:
        zip_codes.append(row['Address'][-5:])
        
# #Debugging
# print(zip_codes)

#Convert zip code to longitude, latitude
nomi = pgeocode.Nominatim('us')
query = nomi.query_postal_code(zip_codes)
coords = {  "lat": query["latitude"],
            "lon": query["longitude"]}
coordinates = pd.DataFrame.from_dict(coords)

#Start of Nick's Code (Subject to change)

#Read in data for heatmap
fname = PROJECT_ROOT_DIR + 'county food insercuity in CA.csv'
county_food_inse = pd.read_csv(fname)

#Debugging
print(county_food_inse['percent'].mean() + 2 * county_food_inse['percent'].std())

# #Create image in browser
values = county_food_inse['percent'].tolist()
fips = county_food_inse['fips'].tolist()
color = ['#c35b7e' , '#910736', '#866ba8', '#f13710', '#f8c928', '#ff8817']

# fig = ff.create_choropleth(
#     fips=fips, values=values, scope=['CA'],
#     binning_endpoints=[6.100608433011778, 9.010649044092098, 11.920689655172417, 14.830730266252736, 17.740770877333055],
#     colorscale=color,
#     county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
#     legend_title='Food Insecurity Percentage by County', title='California Food Insecurity Percentage by County'
# )

# #Using random image and not conforming
california_img = mpimg.imread(os.path.join(PROJECT_ROOT_DIR,'Image','food_inse.png'))
ax = coordinates.plot(kind="scatter", x="lon", y="lat", figsize=(10,7), label="Food Banks")
#extent = [bottom_left_lat, top_right_lat, bottom_left_log, top_right_lat]
plt.imshow(california_img, extent=[-131.25, -107.8, 32, 43])
plt.ylabel("Latitude", fontsize=14)
plt.xlabel("Longitude", fontsize=14)
plt.title("Food Bank Geocoordinates in relation to Food Insecurity Rates")
plt.legend(loc = 'lower right')
plt.show()