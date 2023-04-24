import pandas
import matplotlib.pyplot as plt


data = pandas.read_csv("weather_year.csv")

#Bulk operations with apply()
data.EDT.head()

#Values
first_date = data.EDT.values[0]

first_date

from datetime import datetime
datetime.strptime(first_date, "%Y-%m-%d")

datetime.datetime(2012, 3, 10, 0, 0)

data.date = data.EDT.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))

data.EDT.head()
data.index = data.EDT

print(data)

