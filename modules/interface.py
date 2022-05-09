from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo

from modules.models import cluster, linear_lasso, linear_regression


def display_window():
    """
    It creates a window with a button that opens a file dialog, and a button that executes a function
    depending on the radio button selected by the user
    """

    def import_btn(dialog_title="importer un fichier"):
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

    def import_4_files(dialog_title="importer un fichier"):
        """
        It imports 4 files, and returns them as a tuple

        :param dialog_title: The title of the dialog box, defaults to importer un fichier (optional)
        :return: A tuple of 4 files.
        """
        file_1 = import_btn(dialog_title + "1")
        file_2 = import_btn(dialog_title + "2")
        file_3 = import_btn(dialog_title + "3")
        file_4 = import_btn(dialog_title + "4")
        return file_1, file_2, file_3, file_4

    window = Tk()
    import_label = Label(text="Cliquer pour importer un fichier")
    import_btn = Button(text="import", command=import_btn)

    var = IntVar()
    var.set(1)

    #** Boutons de selection de modeles
    linear_regression_radio_choice = Radiobutton(window,
                                                 text="Régression linéaire",
                                                 variable=var,
                                                 value=1)
    cluster_radio_choice = Radiobutton(window,
                                       text="Clustering",
                                       variable=var,
                                       value=2)

    lasso_radio_choice = Radiobutton(window,
                                     text="LARS Lasso",
                                     variable=var,
                                     value=3)

    def execute_btn():
        """
        It executes the function corresponding to the radio button selected by the user
        """
        try:
            imported_file
        except:
            showinfo("INFO", "Veuillez importer un fichier")
        else:
            if (var.get() == 1):
                linear_regression(imported_file)
            elif (var.get() == 2):
                cluster()
            elif (var.get() == 3):
                linear_lasso(imported_file)
            else:
                showinfo("INFO", "Erreur")

    execute_btn = Button(text="executer", command=execute_btn)

    #* Affichage des éléments dans fenêtre
    import_label.pack()
    import_btn.pack()
    linear_regression_radio_choice.pack()
    cluster_radio_choice.pack()
    lasso_radio_choice.pack()
    execute_btn.pack()

    window.mainloop()
