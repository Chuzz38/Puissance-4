from p4_game import *

class P4_console:
    def __init__(self, nl, nc, joueur1, joueur2)):
        self.nl = 6
        self.nc = 7
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tableJeu = [['0' for i in range(nc)] for j in range(nl)]

    def jeton(self, joueur):
        if joueur == self.joueur1:
            print('@')
        elif joueur == self.joueur2:
            print('X')

    def coup_joueur(self, joueur):
        joueur1 = input("Ecrivez le nom du joueur 1 : ")
        joueur2 = input("Ecrivez le nom du joueur 2 : ")
        print(" ")

    def afficheTableau(self):
        for l in range (nl):
            for c in range (nc):
                print(self.tableJeu[l][c], end = " ")
            print()

    def ajoutePion(self, colonne, joueur):
        P4_game.placer_jeton(colonne, joueur)




"""Il faut définir joueur avant de commencer le jeu"""
joueur = int(input())
#Mieux le définir et demander joueur1 et joueur2
while not P4_game.verifier_victoire(nl, nc, joueur):
        P4_console.afficheTableau()
        print(" ")
        print(joueur,"c'est ton tour")
        print(" ")
        if not P4_game.placement_possible():
            print("Vous devez rejouer")
            colonne = int(input())
        else:
            P4_console.ajoutePion(colonne, joueur)   
        #ne le faire qu'une fois selon le joueur qui joue 

        P4_console.afficheTableau()
        print(" ")
        print(joueur2,"c'est ton tour")
        print(" ")
        if not placement_possible():
            print("Vous devez rejouer")
        else:
            ajoutePion(affichage_pion(joueur), 'X')