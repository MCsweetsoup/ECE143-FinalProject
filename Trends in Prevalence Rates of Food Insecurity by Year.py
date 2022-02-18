from tkinter import Y
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

data = pd.read_excel('Trends in Prevalence Rates of Food Insecurity by Year.xlsx')
data

plt.figure(figsize=(7,7))
year = range(1995, 2021)


#Food Insecure People Plot
plt.plot(data['Food insecurity '], label = r'Food Insecure', c = 'blue')

#Very low food security plot
plt.plot(data['Very low food security'], label = r'Very Low Food Security', c = 'orange')

year = range(1995,2020)

ind = np.arange(len(year))

plt.xticks(ind, year, rotation = 90)
plt.locator_params(axis="x", nbins=8)
plt.ylim(top = 15)
plt.axvline(x = 14, color = 'black', ls = ':', alpha = 0.75)
plt.axvline(x = 6, color = 'black', ls = ':',alpha = 0.75)
plt.axvline(x = 24, color = 'black', ls = ':', alpha = 0.75)
plt.axhline(y = 12, color = 'r', ls = '--' ,alpha = 0.5, )
plt.axhline(y = 5, color = 'red',ls = '--', alpha = 0.5)
plt.legend(loc='upper right')
plt.xlabel("Year")
plt.ylabel("Percent %")
plt.title('Trends in Prevalence Rates of Food Insecurity by Year')
plt.ylim(0, 20)
plt.show()
