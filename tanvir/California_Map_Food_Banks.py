import pandas as pd #For reading in data
import pgeocode #For converting zip code to longitude/latitude
import matplotlib.pyplot as plt #for plotting
from mpl_toolkits.basemap import Basemap

#Change to project directory
PROJECT_ROOT_DIR = "C:\School\ECE_143\ECE_143_Group_Project\\"

#Read in data
fname = PROJECT_ROOT_DIR + 'tanvir\california_foodbanks.csv'
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

# #Debugging
# print(query)
# print(coords)
# print(coords["lat"][0])

# #Purely plotting longitude and latitude histogram style
# coords["lat"].hist()
# plt.title("Latitude of Food Banks")
# plt.show()

# coords["lon"].hist()
# plt.title("Longitude of Food Banks")
# plt.show()

# #Purely plotting longitude and latitude scatter style
# coordinates.plot(kind="scatter", x = 'lon', y = 'lat')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('Bad superposition of geocoordinates of food banks')
# plt.show()

# #Using random image and not conforming
# california_img = mpimg.imread(os.path.join(PROJECT_ROOT_DIR,'prepared_images','california.png'))
# california_img = mpimg.imread("C:\School\ECE_143\Project\prepared_images\california_county_map.jpg")
# ax = coordinates.plot(kind="scatter", x="lon", y="lat", figsize=(10,7), label="Food Banks")
# plt.imshow(california_img, extent=[-122, -113.80, 32.45, 42.05])
# plt.ylabel("Latitude", fontsize=14)
# plt.xlabel("Longitude", fontsize=14)
# plt.title("Bad superposition of geocoordinates of food banks")
# plt.show()

#Plot coordinates in meaningful way
lat = list(coordinates["lat"])
lon = list(coordinates["lon"])
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='c', 
            lat_0=37.5, lon_0=-119,
            width=1E6, height=1.2E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')
m.scatter(lon, lat, latlon = True)
plt.show()
plt.title("Geographical Coordinates of Californian Food Banks")