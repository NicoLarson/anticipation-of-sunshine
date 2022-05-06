from tkinter import *
from modules.files import import_file
from modules.models import cluster, linear_regression


def display_score(model, x_test, y_test, model_test):
    # s = round(model.score(x_test, y_test), 5)
    # MAE = round(mean_absolute_error(y_test, model_test), 5)
    # MBE = round(((y_test - model_test).sum()) / model_test.size, 5)
    # RMSE = round(np.sqrt(mean_squared_error(y_test, model_test)), 5)
    # R2 = round(r2_score(y_test, model_test), 5)
    # maxE = round(max_error(y_test, model_test), 5)
    # score = tk.Label(text="score : " + s.astype(str) + "\n MAE : " +
    #                  MAE.astype(str) + "\n MBE : " + MBE.astype(str) +
    #                  "\n RMSE : " + RMSE.astype(str) + "\n R2 : " +
    #                  R2.astype(str) + "\n maxE : " + maxE.astype(str))
    # score.grid(row=2, column=0)

    # fig = plt.figure(figsize=(3, 2))
    # plt.scatter(y_test, model_test, c='r', label='Predict')
    # plt.plot(y_test, y_test, label='Real')
    # plt.legend()
    # plt.title('Test')
    # plt.xlabel('GHI_Target real')
    # plt.ylabel('GHI_Target predict')
    return False


def display_window():
    """
    It creates a window with a button that, when clicked, calls the function import_file() which opens a
    file dialog and returns the path of the file selected by the user
    """
    window = Tk()

    def execute():
        if (var.get() == 1):
            linear_regression()
        elif (var.get() == 2):
            cluster()
        else:
            print("error")

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
