from tkinter import filedialog
import pandas
import numpy as np


def open_file(dialog_title):
    """
    It opens a file dialog box and returns the file object.

    :param dialog_title: The title of the dialog box
    :return: The file object.
    """
    # takes file location and its type
    file_location = filedialog.askopenfilename(initialdir=r"./datas",
                                               title=dialog_title,
                                               filetypes=(("text files", "*.csv"),
                                                          ("all files", "*.*")))
    # read selected file by dialog box
    file = open(file_location, 'r')
    return file


def open_five_files():
    """
    It opens five files, reads them, and then closes them
    """
    file1 = open_file("Sélectionnez le fichier cible")
    file2 = open_file("Sélectionnez le voisin 1")
    file3 = open_file("Sélectionnez le voisin 2")
    file4 = open_file("Sélectionnez le voisin 3")
    file5 = open_file("Sélectionnez le voisin 4")

    return file1, file2, file3, file4, file5


def read_file(file):
    """
    It reads a csv file, creates a copy of the dataframe, and adds a new column to the copy

    :param file: the file to read
    """
    df = pandas.read_csv(file, sep=';')
    df_copy = df.copy()
    df_copy["GHI(t+1)"] = np.nan
    print(df_copy)
