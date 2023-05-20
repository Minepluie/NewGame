import tkinter as tk
import mysql.connector
from datetime import datetime

def connexion():
    nom_utilisateur = champ_utilisateur.get()
    mot_de_passe = champ_mot_de_passe.get()

    cursor = conn.cursor()
    query = "SELECT * FROM utilisateurs WHERE nom_utilisateur = %s AND mot_de_passe = %s"
    cursor.execute(query, (nom_utilisateur, mot_de_passe))

    result = cursor.fetchone()

    if result:
        print("Connexion réussie")

        # Affichage des champs de l'utilisateur connecté dans les étiquettes
        etiquette_nom_utilisateur.config(text="Nom d'utilisateur : " + result[0])
        etiquette_mot_de_passe.config(text="Mot de passe : " + result[1])
        etiquette_age.config(text="Âge : " + str(result[2]))
        etiquette_date_inscription.config(text="Date d'inscription : " + str(result[3]))
    else:
        print("Échec de la connexion")

    cursor.close()

def inscription():
    nom_utilisateur = champ_utilisateur.get()
    mot_de_passe = champ_mot_de_passe.get()
    age_utilisateur = champ_age.get()
    date_inscription = datetime.now()

    cursor = conn.cursor()
    query = "INSERT INTO utilisateurs (nom_utilisateur, mot_de_passe, age, date_inscription) VALUES (%s, %s, %s, %s)"
    params = (nom_utilisateur, mot_de_passe, age_utilisateur, date_inscription)
    cursor.execute(query, params)
    conn.commit()

    print("Inscription réussie")

    # Affichage des champs de l'utilisateur inscrit dans les étiquettes
    etiquette_nom_utilisateur.config(text="Nom d'utilisateur : " + nom_utilisateur)
    etiquette_mot_de_passe.config(text="Mot de passe : " + mot_de_passe)
    etiquette_age.config(text="Âge : " + age_utilisateur)
    etiquette_date_inscription.config(text="Date d'inscription : " + str(date_inscription))

    cursor.close()

fenetre = tk.Tk()
fenetre.title("Page de connexion/inscription")

conn = mysql.connector.connect(
    host="mysql-minepluie.alwaysdata.net",
    user="minepluie",
    password="Flammouche",
    database="minepluie_connexionjeu"
)

etiquette_utilisateur = tk.Label(fenetre, text="Nom d'utilisateur")
etiquette_utilisateur.pack()

champ_utilisateur = tk.Entry(fenetre)
champ_utilisateur.pack()

etiquette_mot_de_passe = tk.Label(fenetre, text="Mot de passe")
etiquette_mot_de_passe.pack()

champ_mot_de_passe = tk.Entry(fenetre, show="*")
champ_mot_de_passe.pack()

etiquette_age_utilisateur = tk.Label(fenetre, text="Âge")
etiquette_age_utilisateur.pack()

champ_age = tk.Entry(fenetre)
champ_age.pack()

bouton_connexion = tk.Button(fenetre, text="Se connecter", command=connexion)
bouton_connexion.pack()

bouton_inscription = tk.Button(fenetre, text="S'inscrire", command=inscription)
bouton_inscription.pack()

# Étiquettes pour afficher les champs de l'utilisateur connecté ou inscrit
etiquette_nom_utilisateur = tk.Label(fenetre, text="")
etiquette_nom_utilisateur.pack()

etiquette_mot_de_passe = tk.Label(fenetre, text="")
etiquette_mot_de_passe.pack()

etiquette_age = tk.Label(fenetre, text="")
etiquette_age.pack()

etiquette_date_inscription = tk.Label(fenetre, text="")
etiquette_date_inscription.pack()

fenetre.mainloop()

conn.close()
