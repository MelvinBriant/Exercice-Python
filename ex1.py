from math import *
from itertools import permutations

"""EXERCICE 1
nom = input('Votre nom')
print('Bonjour, ' + nom)
"""

"""EXERCICE 2
a = input('Saisissez un nombre')
b = input('Saisissez un deuxième nombre')
c = int(a) + int(b)
print(c)
"""

"""EXERCICE 3
nb1 = input('Saisissez un nombre')
nb2 = input('Saissez un deuxième nombre')
if int(nb1) > int(nb2):
    print(nb1)
else:
    print(nb2)
"""

"""EXERCICE 4
nb = int(input('Saisissez un nombre entier'))
if nb % 2 == 0:
    print('pair')
else:
    print('impair')
"""

"""EXERCICE 5
age = int(input('Saisissez votre âge'))
if age < 18:
    print('Vous êtes Mineur')
else:
    print('Vous êtes Majeur')
"""

def ex6():
    nb1 = int(input('Saisissez un nombre'))
    nb2 = int(input('Saisissez un nombre'))
    nb3 = int(input('Saisissez un nombre'))
    print(max(nb1,nb2,nb3))

def ex7():
    for nb in range(1,101):
        print(nb)


def ex8():
    nb = int(input('Saisissez un nombre'))
    for i in range (1, nb):
        nb = i + nb
    print(nb)

def ex9():
    nb = int(input('Saisissez un nombre'))
    fact = 1
    for i in range(1, nb+1):
        fact = fact * i
    print(nb,'!=',fact)

def ex10():
    rayon = int(input('Saisissez un rayon'))
    perimetre = 2*pi*rayon
    surface = (pi**2)*(rayon**2)
    print("Le périmètre est",perimetre,"et la surface est",surface)

def ex11():
    diviseurs=[]
    nb = int(input('Saisissez un nombre'))
    for i in range(1,nb+1):
        if nb%i==0:
            diviseurs.append(i)
    print(diviseurs)

def ex12v1():
    nb = int(input('Saisissez un nombre'))
    for i in range(1, nb+1):
        print(i,"x",nb)

def ex12v2():
    for j in range(1,10):
        for i in range(1,11):
            print(j,"x",i)

def ex13():
    nb1 = int(input('Saisissez un nombre'))
    nb2 = int(input('Saisissez un deuxième nombre'))
    quotient = nb1 // nb2
    reste = nb1 % nb2
    print("Le reste est", reste,"et le quotient est",quotient)

def ex14():
    nb = int(input('Saisissez un nombre'))
    if sqrt(nb) - int(sqrt(nb)):
        print("Ce n'est pas un carré parfait")
    else:
        print("C'est un carré parfait")

def ex15():
    nb = int(input('Saisissez un nombre'))
    i = 2
    while i < nb and nb % i != 0:
        i += 1

    if i == nb:
        print("Le nombre", nb,"est premier")
    else:
        print("Le nombre", nb,"n'est pas premier")

def ex16():
    var = input("Saisissez un mot")
    motEnChaine = ''
    for i in range(0, len(var)):
        motEnChaine = motEnChaine + var[i] + ' '
    print(motEnChaine)

def ex17():
    var = input("Saisissez un mot")
    lettreDejaVue = []

    for i in range(0, len(var)):
        lettre = var[i]
        nbFois = var.count(var[i])

        if lettre in lettreDejaVue:
            print('---')
        else:
            lettreDejaVue.append(lettre)
            print('Le caractère :', lettre, 'figure', nbFois, 'fois dans le mot')

def ex18():
    var = input("Saisissez un mot")
    lettreATrouvée = False
    for i in range(0, len(var)):
        if var[i] == 'a':
            lettreATrouvée = True
            print('La lettre A a été trouvée en position',i+1)
    if lettreATrouvée == False:
        print('Pas de lettre A de trouvée dans ce mot')

def ex19():
    l = ["laptop","iphone",'tablet']
    for i in range(0, len(l)):
        print(l[i],len(l[i]))

def ex20():
    var = input("Saisissez un mot")
    longueur = len(var)
    premier = var[0]
    dernier = var[longueur-1]
    milieu = var[1:longueur-1]
    motInversé = dernier + milieu + premier
    print(motInversé)

def ex21():
    var = input("Saisissez un mot")
    listeVoyelles=['a','e','i','o','u','y']
    compteurVoyelle = 0
    for i in range(0, len(var)):
        lettre = var[i]
        if lettre in listeVoyelles:
            compteurVoyelle = compteurVoyelle + 1

    print('Il y a', compteurVoyelle,'voyelle(s) dans ce mot')

def ex22():
    var = input("Saisissez une phrase")
    espaceIndex = var.index(" ")
    print(var[0:espaceIndex])

def ex23():
    var = input("Saisissez un fichier")
    extensionIndex = var.index(".")
    longueur = len(var)
    print(var[extensionIndex:longueur+1])

def ex24():
    var = input("Saisissez un mot")
    for i in range(len(var)):
        if var[i] != var[-i-1]:
            print('Le mot', var,'n\'est pas un palindrome')
        else:
            print('Le mot',var,'est un palindrome')

def ex25():
    var = input("Saisissez un mot")
    print(var[::-1])

def ex26():
    var = input("Saisissez un texte")
    res = var.split()

    for i in range(0, int(len(res))):
        if (res[i])[0] == "a":
            print("Le mot",res[i],"commence par la lettre a")

def ex27():
    var = input("Saisissez un texte")
    res = var.split()
    mot = ""

    for i in res:
        if(len(mot)<len(i)):
            mot = i
    print(mot)

def ex28():
    string = input("Saisissez un mot")
    liste = []
    if not liste:
        print("La liste est vide")
    else:
        print("la liste n'est pas vide")
    if len(string) == 0:
        print("Le string est vide")
    else:
        print("Le string n'est pas vide")

def ex29():
    nbrListe = [1,2,3,3,3,2,5,5,3,4,6]
    nbrListe = list(set(nbrListe))
    print(nbrListe)

def ex30():
    enCommun = 0
    list2 = ['1','1','1','1','2','2','2','3','3','3']
    list1 = ['10','0','5']
    for j in range(0, len(list1)):
        for i in range(0, len(list2)):
            if (list1[j] == list2[i]):
                enCommun = enCommun + 1

    if(enCommun != 0):
        print("Ces deux listes ont des valeurs communes")

def ex31():
    list1 = ['1','2','3','4','5','6','7','8','9','10']
    listPair = []
    listImpair = []
    for i in range(0, len(list1)):
        nb = list1[i]
        if int(nb) % 2 == 0:
            listPair.append(nb)
        else:
            listImpair.append(nb)

    print(listPair)
    print(listImpair)

def ex32():
    liste1 = [1, 2, 3]
    print(list(permutations(liste1)))

def ex33():
    var = input("Saisissez un mot")
    longueur = len(var)
    motIndexPair = ""
    for i in range(longueur):
        if int(i) % 2 == 0:
            motIndexPair = motIndexPair + var[i]

    print(motIndexPair)

def ex34():
    notes = [12,4,14,11,18,13,7,10,5,9,15,8,14,16]
    notesAuDessusDeMoyenne = []
    for i in notes:
        if(i>= 10):
            notesAuDessusDeMoyenne.append(i)
    print("La liste des notes au dessus de la moyenne est",notesAuDessusDeMoyenne)

def ex35():
    var = input("Saisissez une liste de mot")
    var = var.split()
    dico = {}
    for mot in var:
        if mot in dico:
            dico[mot] += 1
        else:
            dico[mot] = 1
    print(dico)

def ex36():
    var = input("Saisissez une phrase")
    print(var.replace(' ',''))

def ex37():
    var1 = input("Saisissez une liste de mot")
    var2 = input("Saisissez une deuxième liste de mot")

    liste1 = var1.split()
    liste2 = var2.split()

    listeDeMotsCommuns = set()
    for mot in liste1:
        if mot in liste2:
            listeDeMotsCommuns.add(mot)
    print(listeDeMotsCommuns)

def ex38():
    texte = input("Saisissez un texte")
    liste = texte.split()
    premierMot = liste[0]
    dernierMot = liste[len(liste)-1]
    liste.pop()
    liste.pop(0)
    milieuTexte = " ".join(liste)
    texteV2 = dernierMot + ' ' + milieuTexte + ' ' + premierMot
    print(texteV2)

def ex39():
    texte = input("Saisissez un texte")
    nbMot = len(texte.split())
    print(nbMot)

liste = []
def nombreDivisibles(liste, n):
    nbElementsDivisibles = 0
    for i in range(len(liste)):
        if liste[i] % n == 0:
            nbElementsDivisibles += 1
    return(nbElementsDivisibles)

def nombreOccurences(liste, char):
    nbOccurences = 0
    for i in liste:
        if i == char:
            nbOccurences += 1
    return(nbOccurences)

def insertEtoile(s):
    s2 = ""
    for lettre in s:
        s2 = s2 + lettre + "*"
        longueur = len(s2)
    print(s2[0:longueur-1])

def toutEnMajuscule(liste):
    listeMaj = []
    for lettre in liste:
        listeMaj.append(lettre.upper())
    return(listeMaj)

def ex45(s):
    countMaj = 0
    countMin = 0
    for lettre in s:
        if lettre == lettre.upper():
            countMaj += 1
        else:
            countMin += 1
    print("Il y a", countMaj," majuscules et",countMin,"minuscules dans ce string")

def ex46(nb):

    result = set()
    while nb > 0:
        result |= {nb % 10}
        nb = nb // 10
    return result

T1 = "Python est un langage de programmation"
T2 = "Python est orienté objet"
def ex47(T1, T2):
    listeT1 = T1.split()
    listeT2 = T2.split()
    listeCommun = []
    for mot in listeT1:
        for mot2 in listeT2:
            if mot == mot2:
                listeCommun.append(mot)
    return(listeCommun)


