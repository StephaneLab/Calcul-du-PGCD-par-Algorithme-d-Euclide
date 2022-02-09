#!/usr/bin/python3.9
# Licence MIT copyright (c) 2022 Stéphane Lassalvy
# Algorithme d'Euclide pour le PGCD
def my_PGCD_Euclide(a, b):
    # On écrit les choses de façon à ce que b soit le plus petit des deux nombres
    print("Par convention on fait en sorte que a soit le plus grand des deux nombres, cela n'a pas d'influence sur le résultat car PGCD(a,b) = PGCD(b,a).")
    if a <= b:
        aa = b
        b = a
        a = aa
    # On initialise le pgcd à 0
    pgcd = 0
    # On calcule le reste de la division euclidienne de a par b
    i = 1
    r = a % b
    print(f"Itération {i}, a = ", a, ", b = ", b, ", r = ", r)
    # Si le premier reste est nul, b divise a et le pgcd est b
    if r == 0:
        pgcd = b
        print(f"{b} divise {a} et PGCD({a}, {b}) = ", pgcd)
    # Sinon tant que le reste de la division euclidienne de a par b est >0
    else:
        while  r > 0:
            i = i + 1
            # On prend b pour nouvelle valeur de a
            a = b
            # On prend le reste de la précédente division euclidienne comme nouvelle valeur de b
            b = r
            # On effectue la division euclidienne de a par b
            r = a % b
            print(f"Itération {i}, a = {a}, b = {b}, r = {r}")
            pgcd = b
        # Ainsi le pgcd est le dernier reste non nul calculé par l'algorithme
        print("Le PGCD est le dernier reste non nul :")
        print(f"PGCD = {pgcd}")
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
my_PGCD_Euclide(a, b)