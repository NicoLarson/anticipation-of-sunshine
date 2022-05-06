import numpy as np
import pandas


def data_frame_treatment(data_frame):
    """
    It takes a dataframe, removes the rows that don't have a GHI(t+1) value, and returns the dataframe
    with the GHI(t+1) column, the X and y values for the model, and the original dataframe
    
    :param data_frame: the path to the dataframe
    :return: X, y, df_copy
    """
   
    df = pandas.read_csv(data_frame, sep=';')
    df_copy = df.copy()

    # Traitement des données
    df_copy.loc[:len(df_copy) - 2, "GHI(t+1)"] = np.array(
        df_copy.loc[1:len(df) - 1, "Date"]) - np.array(
            df_copy.loc[:len(df_copy) - 2, "Date"])
    df_copy[(df_copy["GHI(t+1)"] != 1)] = np.nan
    index_with_nan = df_copy.index[df_copy.isnull().any(axis=1)]

    # Nouveau fichier
    df_copy.drop(index_with_nan, 0, inplace=True)
    df_copy = df_copy.append(df.loc[len(df) - 1], ignore_index=True)
    df_copy.loc[:len(df_copy) - 2,
                "GHI(t+1)"] = np.array(df_copy.loc[1:len(df) - 1,
                                                   "GHI(Wh/m2)"])
    df_copy = df_copy[:-1]

    X = df_copy[["Date", "GHI(Wh/m2)"]]
    y = df_copy["GHI(t+1)"]

    return X, y, df_copy
