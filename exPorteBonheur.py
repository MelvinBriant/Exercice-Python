from itertools import permutations

def chiffrePorteBonheur(nb):
    number = nb

    while number > 10:
        nbSplit = list(str(number))
        number = 0
        for chiffre in nbSplit:
            number = int(chiffre) * int(chiffre)
            number += number
    print(number)
    if number == 1:
        print("C'est un nombre lucky")
    else:
        print("Ce n'est pas un nombre lucky")

def generateur(nbFois, lettres):
    lettres1 = list(lettres)
    g2 = ""
    for lettre in lettres1:
        g2 += lettre * nbFois
    print(g2)

def powerset(liste):
    nb = 1
    test = []
    while nb < len(liste)+1:
        test = test + list(permutations(liste, nb))
        nb += 1

    print(test)









