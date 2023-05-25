from tkinter import *
import importlib
def menuplay():
    def import_module_on_click():
        module_name = "Game/LCAT/menu_carte_au_tresor"
        imported_module = importlib.import_module(module_name)
        imported_module.menu_carte()  # Correction ici
        # Vous pouvez maintenant utiliser le module importé selon vos besoins
        
    window = Tk()
    window.title("GamePluie")
    LCAT = Button(window, text="La carte au tresor", command=import_module_on_click)
    quitter = Button(window, text="Quitter", command=window.destroy)
    quitter.pack()
    LCAT.pack()
    window.mainloop()
