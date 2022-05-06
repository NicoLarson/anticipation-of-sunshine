from tkinter import filedialog


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
