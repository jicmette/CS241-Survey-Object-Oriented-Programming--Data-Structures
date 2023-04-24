import pandas as pd #The library that manipulates our data  
import seaborn as sns #Use to plotting and graph
import matplotlib.pyplot as plt #If we need any low level methods

#Load the data
bestb_players = pd.read_csv("basketball_players.csv")
print(bestb_players.head())
print(bestb_players.columns)

#Part 1

#Find the mean (average) and median (is the middle value when a data set
# is ordered from least to greatest) points per season

print("Mean")
print(bestb_players.mean())
print("Median")
print(bestb_players.median())

#Part 2

#Find the highest number of points per season
#Sorted the data set by points and showed the highest 5
print(bestb_players[["playerID", "year", "points"]].sort_values("points", ascending = False).head(5))

#Part 3

#Boxplot of rebounds, points and assists
sns.boxplot(data = bestb_players[["rebounds", "points", "assists"]])
plt.show()

#Part 4

#Grab the points and years and group by year, then find the median 
# of points for each year

year_nbagroup = bestb_players[["points", "year"]].groupby("year").median()
print(year_nbagroup.head())

#Reset the index

year_nbagroup = year_nbagroup.reset_index()
print(year_nbagroup.head())

#Scatter plot
sns.scatterplot(data = year_nbagroup, x = "year", y = "points")
plt.show()