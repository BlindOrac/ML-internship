# Import necessary Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error

# Read Data
df = pd.read_csv('SampleData.csv')
x = df['Parameter 1'].values
y = df['Parameter 2'].values


# mean
def get_mean(arr):
    return np.sum(arr) / len(arr)


# variance
def get_variance(arr, mean):
    return np.sum((arr - mean) ** 2)


# covariance
def get_covariance(arr_x, mean_x, arr_y, mean_y):
    final_arr = (arr_x - mean_x) * (arr_y - mean_y)
    return np.sum(final_arr)


# find coeff
def get_coefficients(x, y):
    x_mean = get_mean(x)
    y_mean = get_mean(y)
    m = get_covariance(x, x_mean, y, y_mean) / get_variance(x, x_mean)
    c = y_mean - x_mean * m
    return m, c


# Regression Function
def linear_regression(x_train, y_train, x_test, y_test):
    prediction = []
    m, c = get_coefficients(x_train, y_train)
    for x in x_test:
        y = m * x + c
        prediction.append(y)

    r2 = r2_score(prediction, y_test)
    mse = mean_squared_error(prediction, y_test)
    print("The R2 score of the model is: ", r2)
    print("The MSE score of the model is: ", mse)
    return prediction


# There are 100 sample out of which 80 are for training and 20 are for testing
linear_regression(x[:80], y[:80], x[80:], y[80:])


# Visualize
def plot_reg_line(x, y):
    prediction = []
    m, c = get_coefficients(x, y)
    for x0 in range(1, 100):
        yhat = m * x0 + c
        prediction.append(yhat)

    fig = plt.figure(figsize=(20, 7))
    plt.subplot(1, 2, 1)
    sns.scatterplot(x=x, y=y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot between X and Y')

    plt.subplot(1, 2, 2)
    sns.scatterplot(x=x, y=y, color='blue')
    sns.lineplot(x=[i for i in range(1, 100)], y=prediction, color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Regression Plot')
    plt.show()


plot_reg_line(x, y)