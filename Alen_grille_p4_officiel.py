from p4_game import *

class P4_console:
    joueur1 = input("Ecrivez le nom du joueur 1 : ")
    joueur2 = input("Ecrivez le nom du joueur 2 : ")
    print(" ")


    colonne = 7
    ligne = 6


    tableau = [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']]

    def afficheTableau(self):
        for l in range (ligne):
            for c in range (colonne):
                print(tableau[l][c], end = " ")
            print()

    def verifieLignes():
        pass


    def ajoutePion(colonne, pion):
        for i in range (LIGNE-1, -1, -1):
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

    