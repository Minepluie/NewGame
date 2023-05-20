from tkinter import *
import mysql.connector as MC
import importlib

def import_module_on_click():
    module_name = "menu_play"
    imported_module = importlib.import_module(module_name)
    imported_module.menuplay()  # Correction ici
    # Vous pouvez maintenant utiliser le module importé selon vos besoins

window = Tk()
window.title("GamePluie")
window.geometry("1080x720")

play = Button(window, text="Play", command=import_module_on_click)
quitter = Button(window, text="Quitter", command=quit)

play.pack()
quitter.pack()

window.mainloop()

print("Le programme a bien été lancé")


