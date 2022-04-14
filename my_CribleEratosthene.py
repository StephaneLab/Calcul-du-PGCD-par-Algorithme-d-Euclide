#!/usr/bin/python3.9
# Licence MIT copyright (c) 2022 Stéphane Lassalvy
import numpy as np
def my_CribleEratosthene(n):
    # Algorithme du crible d'Eratostène pour calculer les nombres premiers inférieur ou égaux à un entier naturel n
    # Il est basé sur le principe qu'un nombre est premier s'il n'est divisible par aucun des nombres premiers qui le précèdent.
    print("On peut considérer par convention que 1 est un nombre premier.")
    nombrePremiers = [2]
    # i est un candidat à être un nombre premier
    i = 3
    while i <= n:
        restes = []
        # Le nombre i est premier s'il n'est pas divisible par les nombre premiers qui le précédent.
        # Pour le savoir, on établit alors la liste des restes des divisions euclidiennes de i par les nombres premiers qui le précèdent.
        for j in nombrePremiers:
            restes.append(i % j)
        # Une fois qu'on a calculé tous les restes, on regarde le reste le plus petit, et s'il est différent de 0,
        # c'est que tous les restes sont différent de 0, et donc que i n'est divisible par aucun des nombres premiers qui le précèdent.
        # On rajoute dans ce cas i à la liste des nombres premiers connus
        if min(restes) > 0:
            nombrePremiers.append(i)
        # et on passe à l'entier i suivant, on ajoute 2 à i car il est inutile de tester les multiples de 2
        i = i + 2
    print(f"Liste des nombres premiers compris dans l'intervalle [2; {n}]:")
    print(nombrePremiers)
# Exécution du programme
n = input("Indiquez le nombre n pour lequels vous voulez calculez les nombres premiers <= n :\n")
n = int(n)
my_CribleEratosthene(n)


