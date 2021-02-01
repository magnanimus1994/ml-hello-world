# import sys
# import scipy
# import numpy
import matplotlib
# import sklearn
import pandas

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(url, names=names)

# print(dataset.shape)
# print(dataset.head(20))
# print(dataset.describe())
# print(dataset.groupby('class').size())

# dataset.plot(kind='box', subplots=True, layout=(2,2), sharey=False)
dataset.hist()
matplotlib.pyplot.show()