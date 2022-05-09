import numpy as np
import pandas


def data_frame_treatment(data_frame):
    """
    It takes a dataframe, creates new columns, calculates the difference between the dates, and then
    fills the new columns with the appropriate values
    
    :param data_frame: the path to the dataframe
    :return: X_fit, Y_fit, X_predict, Y_predict
    """
    df = pandas.read_csv(data_frame, sep=';')
    df_copy = df.copy()

    # création des nouvelles colonnes
    df_copy["GHI(t+1)"] = np.nan
    df_copy["GHI(t-1)"] = np.nan
    df_copy["GHI(t-2)"] = np.nan
    df_copy["GHI(t-3)"] = np.nan
    df_copy["test"] = np.nan

    # calcul du nombre d'heure de difference dans la colonne test
    df_copy.loc[:len(df_copy) - 2, "test"] = np.array(
        df_copy.loc[1:len(df) - 1, "Date"]) - np.array(
            df_copy.loc[:len(df_copy) - 2, "Date"])

    # attribution des valeurs dans les nouvelles colonnes
    df_copy.loc[:len(df_copy) - 2,
                "GHI(t+1)"] = np.array(df_copy.loc[1:len(df) - 1,
                                                   "GHI(Wh/m2)"])
    df_copy.loc[1:len(df_copy) - 1,
                "GHI(t-1)"] = np.array(df_copy.loc[:len(df) - 2, "GHI(Wh/m2)"])
    df_copy.loc[2:len(df_copy) - 1,
                "GHI(t-2)"] = np.array(df_copy.loc[:len(df) - 3, "GHI(Wh/m2)"])
    df_copy.loc[3:len(df_copy) - 1,
                "GHI(t-3)"] = np.array(df_copy.loc[:len(df) - 4, "GHI(Wh/m2)"])

    df_copy[(df_copy["test"] != 1)] = np.nan
    index_with_nan = df_copy.index[df_copy.isnull().any(axis=1)]
    df_copy.drop(index_with_nan, 0, inplace=True)
    df_copy[["heure"]] = (df_copy[["Date"]] % 100).astype(int)
    tab_fit = df_copy[df_copy["Date"] < 2.020e+09]
    tab_score = df_copy[df_copy["Date"] >= 2.020e+09]
    X_fit = tab_fit[[
        "GHI(Wh/m2)", "GHI(t-1)", "GHI(t-2)", "GHI(t-3)", "heure"
    ]].values
    Y_fit = tab_fit["GHI(t+1)"].values
    X_predict = tab_score[[
        "GHI(Wh/m2)", "GHI(t-1)", "GHI(t-2)", "GHI(t-3)", "heure"
    ]].values
    Y_predict = tab_score["GHI(t+1)"].values

    return X_fit, Y_fit, X_predict, Y_predict


def data_frame_treatment_with_cluster(data_frame, df_x_moins_1, df_x_plus_1,
                                      df_y_moins_1, df_y_plus_1):
    df = pandas.read_csv(data_frame, sep=';')
    df_x_moins_1 = pandas.read_csv(df_x_moins_1, sep=';')
    df_x_plus_1 = pandas.read_csv(df_x_plus_1, sep=';')
    df_y_moins_1 = pandas.read_csv(df_y_moins_1, sep=';')
    df_y_plus_1 = pandas.read_csv(df_y_plus_1, sep=';')

    # copie du point principal
    df_copy = df.copy()

    # création des nouvelles colonnes
    df_copy["GHI(t+1)"] = np.nan
    df_copy["GHI(t-1)"] = np.nan
    df_copy["GHI(t-2)"] = np.nan
    df_copy["GHI(t-3)"] = np.nan
    df_copy["test"] = np.nan
    df_copy["y-1"] = df_copy.iloc[:, 2] - df_y_moins_1.iloc[:, 2]
    df_copy["y+1"] = df_copy.iloc[:, 2] - df_y_plus_1.iloc[:, 2]
    df_copy["x-1"] = df_copy.iloc[:, 2] - df_x_moins_1.iloc[:, 2]
    df_copy["x+1"] = df_copy.iloc[:, 2] - df_x_plus_1.iloc[:, 2]

    # calcul du nombre d'heure de difference dans la colonne test
    df_copy.loc[:len(df_copy) - 2, "test"] = np.array(
        df_copy.loc[1:len(df) - 1, "Date"]) - np.array(
            df_copy.loc[:len(df_copy) - 2, "Date"])

    # attribution des valeurs dans les nouvelles colonnes
    df_copy.loc[:len(df_copy) - 2,
                "GHI(t+1)"] = np.array(df_copy.loc[1:len(df) - 1,
                                                   "GHI(Wh/m2)"])
    df_copy.loc[1:len(df_copy) - 1,
                "GHI(t-1)"] = np.array(df_copy.loc[:len(df) - 2, "GHI(Wh/m2)"])
    df_copy.loc[2:len(df_copy) - 1,
                "GHI(t-2)"] = np.array(df_copy.loc[:len(df) - 3, "GHI(Wh/m2)"])
    df_copy.loc[3:len(df_copy) - 1,
                "GHI(t-3)"] = np.array(df_copy.loc[:len(df) - 4, "GHI(Wh/m2)"])

    df_copy[(df_copy["test"] != 1)] = np.nan

    index_with_nan = df_copy.index[df_copy.isnull().any(axis=1)]

    df_copy.drop(index_with_nan, 0, inplace=True)

    df_copy[["heure"]] = (df_copy[["Date"]] % 100).astype(int)

    tab_fit = df_copy[df_copy["Date"] < 2.020e+09]

    tab_score = df_copy[df_copy["Date"] >= 2.020e+09]

    X_fit = tab_fit[[
        "GHI(Wh/m2)", "GHI(t-1)", "GHI(t-2)", "GHI(t-3)", "heure", "y-1",
        "y+1", "x-1", "x+1"
    ]].values
    Y_fit = tab_fit["GHI(t+1)"].values

    X_predict = tab_score[[
        "GHI(Wh/m2)", "GHI(t-1)", "GHI(t-2)", "GHI(t-3)", "heure", "y-1",
        "y+1", "x-1", "x+1"
    ]].values
    Y_predict = tab_score["GHI(t+1)"].values

    return X_fit, Y_fit, X_predict, Y_predict
