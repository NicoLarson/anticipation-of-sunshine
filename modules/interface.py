from tkinter import *
from tkinter import filedialog

from models import cluster, linear_regression


def display_score(model, x_test, y_test, model_test):
    return False


def import_file(dialog_title="importer un fichier"):
    """
    It opens a file dialog, and returns the file object.
    
    :param dialog_title: The title of the dialog box, defaults to importer un fichier (optional)
    :return: The file object.
    """
    global imported_file

    file_location = filedialog.askopenfilename(
        initialdir=r"./datas_test",
        title=dialog_title,
        filetypes=(("text files", "*.csv"), ("all files", "*.*")))
    imported_file = open(file_location, 'r')
    return imported_file
    # showinfo("INFO", "Fichier importé")


def import_4_files(dialog_title="importer un fichier"):
    """
    It imports 4 files, and returns them as a tuple
    
    :param dialog_title: The title of the dialog box, defaults to importer un fichier (optional)
    :return: A tuple of 4 files.
    """
    file_1 = import_file(dialog_title + "1")
    file_2 = import_file(dialog_title + "2")
    file_3 = import_file(dialog_title + "3")
    file_4 = import_file(dialog_title + "4")
    return file_1, file_2, file_3, file_4


def execute():
    if (var.get() == 1):
        linear_regression(imported_file)
    elif (var.get() == 2):
        cluster()
    else:
        print("error")


window = Tk()
import_label = Label(text="Cliquer pour importer un dataframe")
import_btn = Button(text="import", command=import_file)
var = IntVar()
var.set(1)
linear_regression_radio_choice = Radiobutton(window,
                                             text="Régression linéaire",
                                             variable=var,
                                             value=1)
cluster_radio_choice = Radiobutton(window,
                                   text="Clustering",
                                   variable=var,
                                   value=2)

execute_btn = Button(text="executer", command=execute)
import_label.pack()
import_btn.pack()
linear_regression_radio_choice.pack()
cluster_radio_choice.pack()
execute_btn.pack()
window.mainloop()