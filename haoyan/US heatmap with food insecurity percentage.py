"""
Create a US heatmap with food insecurity percentage
"""
import plotly.figure_factory as ff

import numpy as np
import pandas as pd

# data preparation
# df_sample is a data frame which has already contains FIPS of each states and each county
df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']
df_sample.drop(columns=['Year', 'Labor Force', 'Employed', 'Unemployed', 'Unemployment Rate (%)'])

# df_sample store state name and county in the same column we need to separate them in
# order to join the data frame with our own data (only have column "States")
split = df_sample['County Name/State Abbreviation'].str.split(', ').apply(pd.Series)
df_sample['States'] = split[1]

# our own data
state_percentage = pd.read_excel('../States percents.xlsx')

# merge the two data
new = pd.merge(df_sample, state_percentage, on='States')

# You can just comment out those colorscale you don't like

# Accent 5, Accent 6, Accent 4, Accent 1, Accent 3, Accent 2 (from higher percentage to lower percentage)
# colorscale = ['#f8c928', '#ff8817','#f13710','#c35b7e', '#866ba8', '#910736']

# Accent 4, Accent 6, Accent 5, Accent 2, Accent 1, Accent 3 (from higher percentage to lower percentage)
# colorscale = ['#866ba8', '#c35b7e','#910736','#f8c928','#ff8817','#f13710',]

# Accent 4, Accent 2, Accent 6, Accent 5,  Accent 1, Accent 3 (from higher percentage to lower percentage)
# colorscale = ['#866ba8', '#f8c928', '#c35b7e', '#910736', '#ff8817', '#f13710', ]

# different shade of orange/yellow
colorscale = ['#F8D568', '#FFAE42', '#FF9F00', '#FFA500', '#FF8C00', '#F58025', ]


fips = new['FIPS'].tolist()
values = new['Percent'].tolist()

fig = ff.create_choropleth(
    fips=fips, values=values,
    binning_endpoints=[12.0, 15.0, 18.0, 21.0, 24.0],
    colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='Food insecurity rate for each state in 2020',
    legend_title='Percentage'
)

fig.layout.template = None
fig.show()
