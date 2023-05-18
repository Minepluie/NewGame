from tkinter import *
print("Tkinter import")
import mysql.connector as MC
print("Mysql import")
from game import *
window = Tk()
window.mainloop()
window.title("Pas d’idee de nom")
print("Le programme a bien été lancé")
b = Button(window , text = "Play" , command = start())
b.pack()

# connect = MC.
