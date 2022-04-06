from p4_game import *

class P4_console:
    def __init__(self, nl=6, nc=7,jeton=('1','2'), joueur=(1,2)):
        self.nl = nl
        self.nc = nc
        self.jeton = jeton
        self.joueur = joueur 
        self.tableJeu = [['0' for i in range(nc)] for j in range(nl)]

    def demande():
        joueur1 = input("Ecrivez le nom du joueur 1 : ")
        joueur2 = input("Ecrivez le nom du joueur 2 : ")
        print(" ")

    def afficheTableau(self):
        for l in range (nl):
            for c in range (nc):
                print(tableau[l][c], end = " ")
            print()

    def verifieLignes():
        pass


    def ajoutePion(colonne, pion):
        for i in range (nl-1, -1, -1):
            if tableau[i][colonne]==".":
                tableau[i][colonne] = pion
                print("placee en ligne",i)
                break


    while not P4_game.verifier_victoire(ligne, colonne, joueur):
        afficheTableau()
        print(" ")
        print(joueur1,"c'est ton tour")
        print(" ")
        co = int(input("entrer une colonne "))
        if not placement_possible():
            print("Vous devez rejouer")
        else:
            ajoutePion(co, '@')
        

        afficheTableau()
        print(" ")
        print(joueur2,"c'est ton tour")
        print(" ")
        co = int(input("entrer une colonne "))
        if not placement_possible():
            print("Vous devez rejouer")
        else:
            ajoutePion(co, 'X')

    