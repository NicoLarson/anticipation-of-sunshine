from tkinter import *

from modules.models import traitement_cluster
from modules.models import traitement_test

# Traitement un fichier


def display_result():
    """
    Display the result of the calculation.
    """
    text.insert('1.0', "Resultat du traitement du fichier 1 : \n")
    text.insert('2.0', "Resultat du traitement du fichier : \n")
    text['state'] = 'disabled'

    return "Premier traitement du fichier ok"


def display_app():
    # Créer une fenêtre Tkinter
    gui_win = Tk()
    gui_win.geometry('600x600')
    gui_win.title('TER - Traitement et évaluation de données')

    # Traiter le fichier
    import_btn = Button(gui_win, text="Traiter un fichier",
                        command=traitement_test)
    cluster_btn = Button(
        gui_win, text="Traitement avec les voisins", command=traitement_cluster)

    import_btn.pack()
    cluster_btn.pack()

    text = Text(gui_win, height=2)
    text.pack()
    
    gui_win.mainloop()
