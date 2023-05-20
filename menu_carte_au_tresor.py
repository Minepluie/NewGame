from tkinter import *
import game

def menu_carte():   
    window = Tk()
    window.title("La Carte au Tresor")
    start_btn = Button(window, text="Play", command=game.game)
    start_btn.pack()
    window.mainloop()