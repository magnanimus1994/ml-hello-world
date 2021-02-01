# import sys
# import scipy
# import numpy
import matplotlib
import sklearn.model_selection
import sklearn.metrics
import pandas

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(url, names=names)

# Dataset Info
# print(dataset.shape)
# print(dataset.head(20))
# print(dataset.describe())
# print(dataset.groupby('class').size())

# Plotting Data
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharey=False)
# dataset.hist()
# pandas.plotting.scatter_matrix(dataset)
# matplotlib.pyplot.show()

array = dataset.values
x = array[:, 0:4]
y = array[:, 4]
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(x, y, test_size=0.20, random_state=1)
