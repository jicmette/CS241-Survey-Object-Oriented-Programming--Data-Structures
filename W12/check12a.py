import pandas


data = pandas.read_csv("census.csv")

median = data.median()
max = data.max()
mean = data.mean()

print(median)
print(mean)
print(max)
