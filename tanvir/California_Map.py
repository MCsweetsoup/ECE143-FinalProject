import pandas as pd #For reading in data
import pgeocode #For converting zip code to longitude/latitude
import matplotlib.pyplot as plt #for plotting
import numpy as np
from matplotlib import cm
import plotly.figure_factory as ff

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

data = pd.read_csv('poverty.csv')

