from matplotlib import pyplot as plt
import numpy as np
import pandas
from sklearn.linear_model import LinearRegression


def data_frame_treatment(data_frame):
    """
    It takes a dataframe, and returns a new dataframe with the same columns, but with the rows that are
    not consecutive removed
    
    :param data_frame: the dataframe that you want to treat
    :return: A dataframe with the same columns as the input dataframe, but with the last column being
    the GHI(t+1) column.
    """
    data_frame = pandas.read_csv(data_frame, sep=';')
    data_frame_new = data_frame.copy()

    data_frame_new["GHI(t+1)"] = np.nan
    data_frame_new.loc[:len(data_frame_new) - 2, "GHI(t+1)"] = np.array(
        data_frame_new.loc[1:len(data_frame) - 1, "Date"]) - np.array(
            data_frame_new.loc[:len(data_frame_new) - 2, "Date"])
    data_frame_new[(data_frame_new["GHI(t+1)"] != 1)] = np.nan
    index_with_nan = data_frame_new.index[data_frame_new.isnull().any(axis=1)]
    data_frame_new.drop(index_with_nan, 0, inplace=True)
    data_frame_new = data_frame_new.append(data_frame.loc[len(data_frame) - 1],
                                           ignore_index=True)

    data_frame_new.loc[:len(data_frame_new) - 2, "GHI(t+1)"] = np.array(
        data_frame_new.loc[1:len(data_frame) - 1, "GHI(Wh/m2)"])
    return data_frame_new


def linear_regression(file):
    data_frame = data_frame_treatment(file)
    print(data_frame)
    plt.plot(data_frame["Date"], data_frame["GHI(t+1)"])
    plt.show()
    # model = LinearRegression()
    # X = data_frame[["Date", "GHI(Wh/m2)"]]
    # y = data_frame["GHI(t+1)"]
    # plt.scatter(X, y)
    # plt.show()


def cluster():
    print("cluster")
    return "cluster"