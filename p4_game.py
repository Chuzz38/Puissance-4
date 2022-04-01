import random
"""On va créer une classe puissance 4 qui aura les différents attributs
et les différentes méthodes pour rendre le puissance 4 possible"""


"""
0 : case vide ; 1 : case du joueur 1 ; 2 : case du joueur 2
pour pouvoir stocker au fur et mesure du jeu"""

"""tester à chaque fois si il y a victoire et si c'est vide on ne peut pas mettre au dessus : retourne si """

class P4_game:
    def __init__(self, nl=6, nc=7,jeton=('1','2')):
        self.nl = nl
        self.nc = nc
        self.jeton = jeton
        self.tableJeu = [['0' for i in range(nc)] for j in range(nl)]
        self.nouvellepartie(self.nl, self.nc, self.jeton)

    def get_case(self, ligne, colonne):
        return self.tableJeu[ligne][colonne]

    def placement_possible(self, colonne):
        """Prend en parametre seulement la colonne et renvoie 
        True si la case est libre et False sinon"""
        return self.tableJeu[0][colonne] == 0 

    def placer_jeton(self, joueur, colonne):
        """ Joue le coup du joueur dans la colonne choisie.
        Si la colonne n'est pas disponible il faut choir une autre colonne
        """
        if not placement_possible(colonne, joueur): 
            print("Vous ne pouvez pas jouer dans cette colonne")
        else:
            self.tableJeu[self.ligne][colonne] == self.jeton[joueur-1]

    def verifier_victoire(self, ligne, colonne, joueur):
        """ vérifie si le dernier coup joué, qui a placé le jeton
        de joueur en (ligne,colonne) permet de gagner, on devra 
        tester toutes les combinaisons possibles : colonne, ligne
        et diagonales
        """
        victoire = False
        victoirePossible = self.jeton[joueur-1] * 4 #on donne la combinaison pour que ça soit gagné
        #vérifier si la ligne est correcte
        ligne_tableJeu = [ligne[colonne]for colonne in self.tableJeu]
        while not victoire:
            

    def nouvellepartie(self, nl=6, nc=7, jeton =('1', '2'))
        pass

if __name__ == "__main__":
