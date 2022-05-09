from matplotlib import pyplot as plt
import pandas
from sklearn.linear_model import Lasso, LinearRegression
from modules.data_treatment import data_frame_treatment


def linear_regression(X_fit, Y_fit, X_predict, Y_predict):
    model = LinearRegression()
    fit = model.fit(X_fit, Y_fit)
    X_result = model.predict(X_predict)
    score_predict = model.score(X_predict, Y_predict)
    print(score_predict)
    score_fit = fit.score(X_fit, Y_fit)
    print(score_fit)
    return [score_predict, score_fit]


def linear_lasso(file):
    """
    It takes a file as input, and returns a dataframe with the predicted values
    
    :param file: the name of the file to be used
    """
    X, y, data_frame = data_frame_treatment(file)
    lasso = Lasso(alpha=0.1)
    lasso.fit(X, y)
    score = lasso.score(X, y)
    y_pred = lasso.predict(X)
    result = pandas.DataFrame({"Date": data_frame["Date"], "GHI(t+1)": y_pred})
    score = round(score, 2)
    title = "Lasso regression score: " + str(score)
    display_result(result, title)


# TODO: Ajouter la fonction du traitement avec les voisins
def cluster():
    print("cluster")
    return "cluster"


def display_result(result, title):
    """
    It takes a dataframe and a title, and plots the dataframe's "Date" column against its "GHI(t+1)"
    column
    
    :param result: the dataframe containing the predicted values
    :param title: The title of the plot
    """
    plt.title(title)
    plt.plot(result["Date"], result["GHI(t+1)"])
    plt.show()