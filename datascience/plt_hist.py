#%% 
# https: // towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0

import seaborn as sns
import pandas as pd

flights = pd.read_csv("../data/formatted_flights.csv")
flights.head(10)

#%% 绘制航班延误时间的直方图
import pandas as pd
import matplotlib.pyplot as plt

plt.hist(flights['arr_delay'],color='blue',
    edgecolor='black', bins= int(180/5), density=True)

plt.title("Histogram of Arrival Delays")
plt.xlabel("Delay (min)")
plt.ylabel("Flights")

#%% 绘制航班延误时间的直方图, 根据航班分类
# Make a separate list for each airline
x1 = list(flights[flights['name'] == 'United Air Lines Inc.']['arr_delay'])
x2 = list(flights[flights['name'] == 'JetBlue Airways']['arr_delay'])
x3 = list(flights[flights['name'] == 'ExpressJet Airlines Inc.']['arr_delay'])
x4 = list(flights[flights['name'] == 'Delta Air Lines Inc.']['arr_delay'])
x5 = list(flights[flights['name'] == 'American Airlines Inc.']['arr_delay'])

# Assign colors for each airline and the names
colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00']
names = ['United Air Lines Inc.', 'JetBlue Airways', 'ExpressJet Airlines Inc.',
         'Delta Air Lines Inc.', 'American Airlines Inc.']

plt.hist([x1, x2, x3, x4, x5], bins=int(180/15), color=colors, label=names)

plt.legend()
plt.xlabel('Delay (min)')
plt.ylabel('Mormalized Flights')
plt.title('Side-by-Side Histogram with Multiple Airlines')

#%% 绘制航班延误时间的直方图, 根据航班分类, stacked

plt.hist([x1, x2, x3, x4, x5], bins=int(180/10), stacked=True,
        color=colors, label=names)

plt.legend()
plt.xlabel('Delay (min)')
plt.ylabel('Mormalized Flights')
plt.title('Side-by-Side Histogram with Multiple Airlines')

#%%
# List of five airlines to plot
airlines = ['United Air Lines Inc.', 'JetBlue Airways', 'ExpressJet Airlines Inc.',
            'Delta Air Lines Inc.', 'American Airlines Inc.']

# Iterate through the five airlines
for airline in airlines:
    # Subset to the airline
    subset = flights[flights['name'] == airline]

    # Draw the density plot
    sns.distplot(subset['arr_delay'], hist=False, kde=True,
                 kde_kws={'linewidth': 2},
                 label=airline)

# Plot formatting
plt.legend(prop={'size': 10}, title='Airline')
plt.title('Density Plot with Multiple Airlines')
plt.xlabel('Delay (min)')
plt.ylabel('Density')
#%%
plt.hist([x1, x2, x3, x4, x5], bins=int(180/10), density=True,
         color=colors, label=names)

plt.legend()
plt.xlabel('Delay (min)')
plt.ylabel('Mormalized Flights')
plt.title('Side-by-Side Histogram with Multiple Airlines')


#%% Density plot with rug plot

# Subset to Alaska Airlines
subset = flights[flights['name'] == 'Alaska Airlines Inc.']

# Density Plot with Rug Plot
sns.distplot(subset['arr_delay'], hist=False, kde=True, rug=True,
             color='darkblue',
             kde_kws={'linewidth': 3},
             rug_kws={'color': 'black'})

# Plot formatting
plt.title('Density Plot with Rug Plot for Alaska Airlines')
plt.xlabel('Delay (min)')
plt.ylabel('Density')
