import math

class Domino :
    # Initialisation de la classe
    def __init__(self,A,B):
        self.A = A
        self.B = B

    def affiche_points(self):
        print("face A : " + str(self.A) + ", face B : " + str(self.B))

    def totale(self):
        return self.A + self.B

    def __repr__(self):
        return repr(self.A + self.B)

#if __name__ == '__main__':
   # d = Domino(4,6)
   # d.affiche_points()
   # x = d.totale()
   # print(x)

class CompteBancaire :
    # Initialisation de la classe
    def __init__(self,nomTitu,solde=0):
        self.nomTitu = nomTitu
        self.solde = solde

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        self.solde -= somme

    def affiche(self):
        print("Votre solde courant est de " + str(self.solde))

    def __repr__(self):
        return repr(self.nomTitu + self.solde)


#if __name__ == '__main__':
    # compte1 = CompteBancaire('Jean', 1000)
    # compte1.retrait(200)
    # compte1.affiche()

    # compte2 = CompteBancaire('Marc')
    # compte2.depot(500)
    # compte2.affiche()

class TableMultiplication :
    # Initialisation de la classe
    def __init__(self, number):
        self.number = number
        self.generator = (self.number * x for x in range(1, 10))

    def prochain(self):
        return next(self.generator)

    def __repr__(self):
        return repr(self.number + self.generator)


class Fraction :
    # Initialisation de la classe
    def __init__(self, num, num2):
        self.num = num
        self.num2 = num2


    def affiche(self):
        print(str(self.num) + "/" + str(self.num2))

    def calcul(self):
        return math.gcd(self.num, self.num2)

    def __repr__(self):
        return repr(self.num + self.num2)
