# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:35:13 2022

@author: eliott
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importation d'une base de donnée concernant les émissions de gaz à effet de serre des pays dans le monde entre 1990 à 2018
df = pd.read_csv("ALL GHG_historical_emissions.csv")
df

# On récupère les 10 plus grands pays émetteur de GES en 2018
# (On ne récupère pas les données concernant le monde et l'Union Européenne.)
Chine_gaz = df['2018'][1]
USA_gaz = df['2018'][2]
India_gaz = df['2018'][3]
Russia_gaz = df['2018'][5]
Indonesia_gaz = df['2018'][6]
Brazil_gaz = df['2018'][7]
Japan_gaz = df['2018'][8]
Iran_gaz = df['2018'][9]
Allemagne_gaz = df['2018'][10]
Canada_gaz = df['2018'][11]

# On les classes dans un tableau. 
liste_10_pays_gaz = [Chine_gaz,USA_gaz, India_gaz, Russia_gaz,Indonesia_gaz,Brazil_gaz,Japan_gaz,Iran_gaz,Allemagne_gaz,Canada_gaz]

# On récupère les statistiques démographiques de 2018 (En million d'habitant) 
# concernant les 10 plus grands pays émetteur de GES. 
Chine_pop = 1393.0
USA_pop = 326.8
India_pop = 135.3
Russia_pop = 144.5
Indonesia_pop = 267.7
Brazil_pop = 209.5
Japan_pop = 126.5
Iran_pop = 81.1
Allemagne_pop = 82.91
Canada_pop = 37.07

# On les classes dans un tableau.
liste_pop = np.array([Chine_pop,USA_pop,India_pop,Russia_pop,Indonesia_pop,Brazil_pop,Japan_pop,Iran_pop,Allemagne_pop,Canada_pop])

# On établit la liste des 10 plus grands pays émetteur de GES.
liste_10_pays = ["Chine","USA", "Inde", "Russie","Indonésie","Brésil","Japon","Iran","Allemagne","Canada" ]

# On établit une nouvelle base de donnée avec seulement les informations
# qui nous seront utiles pour nos analyses de données.
# la liste des 10 plus grands pays émetteur de GES.
# leur consomation en MtECO2, et leur population total en millions d'habitants
d = {'Country': liste_10_pays, '2018': liste_10_pays_gaz, 'population en M' : liste_pop}
GES_par_Pays = pd.DataFrame(data=d)
GES_par_Pays
# Nous avons maintenant un tableau trié en fonction de 
# l'émission des GES en MtECO2 des 10 pays. 

# On veut maintenant récupérer la consommation par habitant en KgECO2.
# Que l'on stock dans la variable: Consomation_par_habitant_kg.
Consomation_par_habitant_Mt = (liste_10_pays_gaz)/(np.power(10,6)*liste_pop)
Consomation_par_habitant_kg = np.power(10,9)*Consomation_par_habitant_Mt

# On réalise une nouvelle base de données, cependant avec comme valeurs
# la consommation par habitant des 10 plus grands pays émetteur de GES.
d = {'Country': liste_10_pays, '2018': Consomation_par_habitant_kg, 'population en M' : liste_pop}
GES_par_Habitant = pd.DataFrame(data=d)
GES_par_Habitant

# On trie le tableau GES_par_Habitant par rapport à la colonne 2018 par ordre 
# décroissant. On stock cette valeur dans la variable GES_par_Habitant_tri.
GES_par_Habitant_tri = GES_par_Habitant.sort_values(by = '2018', ascending = False)

# On réalise un diagramme à barre.
# Montrant la consommation en KgECO2 des GES par habitant des 10 plus grand
# pays émetteur de GES en 2018.
plt.figure(figsize=(12,5))
plt.bar(GES_par_Habitant_tri['Country'], GES_par_Habitant_tri['2018'])
plt.xlabel("10 plus gros pays émetteur de GES")
plt.ylabel("Kilogramme équivalent CO2 des GES")
plt.title("Consommation en KgECO2 des GES par habitant des 10 plus grands pays émetteur de GES en 2018")
plt.show()

# On réalise un diagramme à barre.
# Montrant la consommation des 10 plus grands émetteur de GES dans le monde.
plt.figure(figsize=(12,5))
plt.bar(GES_par_Pays['Country'], GES_par_Pays['2018'])
plt.xlabel("Pays")
plt.ylabel("Mégatonne équivalent CO2 des GES")
plt.title("Consommation en MtECO2 des GES des 10 plus grands pays émetteur de MtECO2 en 2018")
plt.show()