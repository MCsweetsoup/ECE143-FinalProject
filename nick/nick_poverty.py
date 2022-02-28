import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import plotly.figure_factory as ff
import folium
import json
# %matplotlib inline

# load poverty of California by county dataset
data = pd.read_csv('poverty.csv')
# print(data)

# load estimate by county name 
estimate_by_county = data.loc[data['race_eth_name'] == 'Total'][['estimate', 'county_name']]
estimate_by_county = estimate_by_county.dropna()
avg_est_county = estimate_by_county.groupby('county_name').mean()
top10_est_county = avg_est_county.sort_values(by=['estimate'], ascending=False).head(10)
# print(top10_est_county)

# top 10 county with estimated poverty percentage
plt.figure(figsize=(10, 8))

x = list(top10_est_county.index)
y = top10_est_county['estimate']
for i in range(len(x)):
    plt.bar(x[i], y[i], color=cm.jet(1. * (len(x) - i) / len(x)))
plt.xlabel('county name')
plt.ylabel('estimated percent of families in poverty')
plt.title('top 10 county with respective estimated poverty percentage')


# group estimate by race
estimate_by_race = data[['estimate', 'race_eth_name']]
estimate_by_race = estimate_by_race.dropna()
avg_est_race = estimate_by_race.groupby('race_eth_name').mean()
# print(avg_est_race)

# poverty percentage w.r.t race 
plt.figure(figsize=(10, 8))

x = list(avg_est_race.index)
y = avg_est_race['estimate']
for i in range(len(x)):
    plt.bar(x[i], y[i], color=cm.jet(1. * (len(x) - i) / len(x)))
plt.xlabel('race/ethnicity')
plt.ylabel('estimated percent of families in poverty')
plt.title('percentage of families in poverty over different races')



# poverty heatmap by county
estimate_by_county = data.loc[data['race_eth_name'] == 'Total'][['estimate', 'county_name', 'county_fips']]
estimate_by_county = estimate_by_county.dropna()
avg_est_county = estimate_by_county.groupby('county_name').mean()
avg_est_county['county_fips'] = avg_est_county['county_fips'].astype(int)
# print(avg_est_county)

values = avg_est_county['estimate'].tolist()
fips = avg_est_county['county_fips'].tolist()
color = ['#c35b7e' , '#910736', '#866ba8', '#f13710', '#f8c928', '#ff8817']

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    binning_endpoints=[17.394022, 27.569496, 37.74497, 47.920444, 58.095918],
    colorscale=color,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Poverty Level by County', title='California Poverty Level by County'
)
fig.layout.template = None
fig.show()

