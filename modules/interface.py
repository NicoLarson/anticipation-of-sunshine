from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
from modules.data_treatment import data_frame_treatment, data_frame_treatment_with_cluster

from modules.models import linear_lasso, linear_regression, svr


def open_file(dialog_title):
    """
    It opens a file dialog box and returns the file object.
    
    :param dialog_title: The title of the dialog box
    :return: The file object.
    """
    # takes file location and its type
    file_location = filedialog.askopenfilename(
        initialdir=r"./datas",
        title=dialog_title,
        filetypes=(("text files", "*.csv"), ("all files", "*.*")))
    # read selected file by dialog box
    file = open(file_location, 'r')
    return file


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

        imported_file = open_file("Importer un fichier")

        return imported_file

    def import_4_files():
        global df_x_moins_1
        df_x_moins_1 = open_file("Sélectionner le fichier df_x_moins_1")
        global df_x_plus_1
        df_x_plus_1 = open_file("Sélectionner le fichier df_x_plus_1")
        global df_y_moins_1
        df_y_moins_1 = open_file("Sélectionner le fichier df_y_moins_1")
        global df_y_plus_1
        df_y_plus_1 = open_file("Sélectionner le fichier df_y_plus_1")

    window = Tk()
    window.geometry('600x600')
    window.title('TER - Traitement et évaluation de données')
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="orange", background="white")

    import_btn = Button(text="importer un fichier", command=import_btn)

    #** Boutons option voisins **#

    cluster_var = IntVar()
    cluster_var.set(1)
    without_cluster_radio_choice = Radiobutton(window,
                                               text="Sans voisins",
                                               variable=cluster_var,
                                               value=1)
    cluster_radio_choice = Radiobutton(window,
                                       text="Avec voisins",
                                       variable=cluster_var,
                                       value=2)

    #** Boutons de selection de modeles **#

    var = IntVar()
    var.set(1)

    linear_regression_radio_choice = Radiobutton(window,
                                                 text="Régression linéaire",
                                                 variable=var,
                                                 value=1)

    lasso_radio_choice = Radiobutton(window,
                                     text="LARS Lasso",
                                     variable=var,
                                     value=2)
    svr_radio_choice = Radiobutton(window,
                                   text="Support Vector Regression",
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
            if cluster_var.get() == 1:
                X_fit, Y_fit, X_predict, Y_predict = data_frame_treatment(
                    imported_file)
                if (var.get() == 1):
                    linear_regression(X_fit, Y_fit, X_predict, Y_predict)
                elif (var.get() == 2):
                    linear_lasso(X_fit, Y_fit, X_predict, Y_predict)
                elif (var.get() == 3):
                    svr(X_fit, Y_fit, X_predict, Y_predict)
                else:
                    showinfo("INFO", "Erreur")
            elif cluster_var.get() == 2:
                import_4_files()
                X_fit, Y_fit, X_predict, Y_predict = data_frame_treatment_with_cluster(
                    imported_file, df_x_moins_1, df_x_plus_1, df_y_moins_1,
                    df_y_plus_1)
                if (var.get() == 1):
                    linear_regression(X_fit, Y_fit, X_predict, Y_predict)
                elif (var.get() == 2):
                    linear_lasso(X_fit, Y_fit, X_predict, Y_predict)
                elif (var.get() == 3):
                    svr(X_fit, Y_fit, X_predict, Y_predict)
                else:
                    showinfo("INFO", "Erreur")

    execute_btn = Button(text="executer", command=execute_btn)

    #* Affichage des éléments dans fenêtre
    Label(window, text='Importer le fichier principal :', fg='black', pady=10)
    import_btn.pack()
    Label(text="Avec ou sans voisin").pack()
    without_cluster_radio_choice.pack()
    cluster_radio_choice.pack()
    Label(text="Les modèles").pack()
    linear_regression_radio_choice.pack()
    lasso_radio_choice.pack()
    svr_radio_choice.pack()
    execute_btn.pack()

    window.mainloop()
