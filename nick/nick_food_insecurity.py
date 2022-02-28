import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import plotly.figure_factory as ff
import folium
import json
# %matplotlib inline

# load food insecurity level by county
county_food_inse = pd.read_csv('county food insercuity in CA.csv')

# print(county_food_inse['percent'].mean() + 2 * county_food_inse['percent'].std())

# food insecurity level by county
values = county_food_inse['percent'].tolist()
fips = county_food_inse['fips'].tolist()
color = ['#c35b7e' , '#910736', '#866ba8', '#f13710', '#f8c928', '#ff8817']

# generate heatmap of food insecurity of CA county
fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    binning_endpoints=[6.100608433011778, 9.010649044092098, 11.920689655172417, 14.830730266252736, 17.740770877333055],
    colorscale=color,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Food Insecurity Percentage by County', title='California Food Insecurity Percentage by County'
)
fig.layout.template = None
fig.show()

