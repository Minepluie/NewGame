from tkinter import *
import mysql.connector as MC
import game
import smtplib
window = Tk()
window.mainloop()
window.title("Pas d’idee de nom")
window.geometry("480x360")
window.minsize(480, 360)
window.maxsize(1080, 720)

print("Le programme a bien été lancé")
# connect = MC.