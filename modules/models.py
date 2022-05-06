import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression

from modules.files import open_file
from modules.files import open_five_files
from modules.files import read_file


def traitement_cluster():
    """
    It opens five files and prints a message
    :return: The string "Traitement avec les voisins ok"
    """
    print("Traitement avec les voisins")
    file1, file2, file3, file4, file5 = open_five_files()
    read_file(file1)
    read_file(file2)
    read_file(file3)
    read_file(file4)
    read_file(file5)
    print("Traitement avec les voisins ok")
    return "Traitement avec les voisins ok"


def traitement_test():
    file_x = open_file("Sélectionner le fichier X à traiter")
    file_y = open_file("Sélectionner le fichier Y à traiter")

    file_x_prediction = open_file("Sélectionner le fichier X prediction")
    file_y_prediction = open_file("Sélectionner le fichier Y prediction")
    # Les données
    X = pd.read_csv(file_x, sep=';')
    y = pd.read_csv(file_y, sep=';')

    X_prediction = pd.read_csv(file_x_prediction, sep=';')
    y_test = pd.read_csv(file_y_prediction, sep=';')

    X = X[['Date', 'GHI(Wh/m2)']]
    y = y[['GHI(Wh/m2)']]

    X_prediction = X_prediction[['Date', 'GHI(Wh/m2)']]
    y_test = y_test[['GHI(Wh/m2)']]

    print(X)
    print(y)

    model = LinearRegression()
    model.fit(X, y)
    score = model.score(X, y)

    prediction = model.predict(X_prediction)
    score_predict = model.score(prediction, y_test)

    print(y_test)
    print(prediction)

    # plt.subplot(1, 2, 1)
    # plt.plot(X[['Date']].values, y.values, label='GHI')
    # plt.legend()
    # plt.title('Brut')
    # plt.xlabel('hour')
    # plt.ylabel('value')
    # plt.show()

    return "Premier traitement du fichier ok"
