#!/usr/bin/python3.9
# Licence MIT copyright (c) 2022 Stéphane Lassalvy
# Algorithme des différences successives pour le PGCD
def my_PGCD_Differences(a, b):
    # On écrit les choses de façon à ce que b soit le plus petit des deux nombres
    print("Par convention on fait en sorte que a soit le plus grand des deux nombres, cela n'a pas d'influence sur le résultat car PGCD(a,b) = PGCD(b,a).")
    if a <= b:
        aa = b
        b = a
        a = aa
        print(f"On veut calculer PGCD({a}, {b})")
    # On initialise le pgcd à 0
    pgcd = 0
    # On calcule la différence a - b
    d = a - b
    i = 0
    while(d > 0):
         i = i + 1
         newa = min(a, b)
         newb = d
         a = newa
         b = newb
         if a <= b:
            aa = b
            b = a
            a = aa
         print(f"Itération {i}, d = {d}, ceci qui revient à calculer le PGCD({a}, {b})")
         d = a - b
    # Si d est nulle le PGCD et le a (ou b puisqu'ils sont égaux) précédents
    if d == 0:
         pgcd = a
         print(f"d = {d}, a et b sont égaux, PGCD({a}, {b}) = {pgcd}")
    # Si le pgcd vaut 1, alors on dit que les deux nombres sont premiers entre eux
    if pgcd == 1:
        print()
        print("a et b sont premiers entre eux")
# Saisie des coefficients du trinôme
print("Saisie des deux nombre entier a et b dont on veut calculer le PGCD.")
a = input("Entrez le nombre entier a : ")
b = input("Entrez le nombre entier b : ")
# Conversion des réponses alphanumériques en numériques (réels)
a = int(a)
b = int(b)
# Exécution de la fonction _my_Trinome_Term
my_PGCD_Differences(a, b)
