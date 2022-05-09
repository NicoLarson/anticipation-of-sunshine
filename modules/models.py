from matplotlib import pyplot as plt
import numpy as np
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.svm import SVR
from modules.data_treatment import data_frame_treatment


def linear_regression(X_fit, Y_fit, X_predict, Y_predict):
    model = LinearRegression()
    fit = model.fit(X_fit, Y_fit)
    score_predict = model.score(X_predict, Y_predict)
    score_fit = fit.score(X_fit, Y_fit)
    print("Score de la prédiction : ", round(score_predict, 2))
    print("Score de l’entraînement : ", round(score_fit, 2))
    display_result("Régression linéaire", score_predict, score_fit)
    return [score_predict, score_fit]


def svr(X_fit, Y_fit, X_predict, Y_predict):
    model = SVR()
    fit = model.fit(X_fit, Y_fit)
    score_predict = model.score(X_predict, Y_predict)
    score_fit = fit.score(X_fit, Y_fit)
    print("Score de la prédiction : ", round(score_predict, 2))
    print("Score de l’entraînement : ", round(score_fit, 2))
    display_result("Support Vector Regression", score_predict, score_fit)
    return [score_predict, score_fit]


def linear_lasso(X_fit, Y_fit, X_predict, Y_predict):
    model = Lasso()
    fit = model.fit(X_fit, Y_fit)
    score_predict = model.score(X_predict, Y_predict)
    score_fit = fit.score(X_fit, Y_fit)
    print("Score de la prédiction : ", round(score_predict, 2))
    print("Score de l’entraînement : ", round(score_fit, 2))
    display_result("LARS Lasso", score_predict, score_fit)
    return [score_predict, score_fit]


def display_result(title, score_predict, score_fit):
    plt.title(title)
    plt.plot(score_predict, score_fit)
    plt.show()