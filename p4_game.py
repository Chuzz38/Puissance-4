"""On va créer une classe puissance 4 qui aura les différents attributs
et les différentes méthodes pour rendre le puissance 4 possible"""


"""
0 : case vide ; 1 : case du joueur 1 ; 2 : case du joueur 2
pour pouvoir stocker au fur et mesure du jeu"""

"""tester à chaque fois si il y a victoire et si c'est vide on ne peut pas mettre au dessus : retourne si """

class P4_game:
    def __init__(self, nl=6, nc=7 ):
        self.nl = nl
        self.nc = nc
        self.joueur = 1 
        self.tableJeu = [['0' for i in range(nc)] for j in range(nl)]

    def joueur_suivant(self):
        self.joueur %= 2 
        self.joueur += 1 

    def get_case(self, ligne, colonne):  # pour une colonne renvoyer la ligne
        return self.tableJeu[ligne][colonne]

    def placement_possible(self, colonne):
        """Prend en parametre seulement la colonne et renvoie 
        True si la case est libre et False sinon"""
        return self.tableJeu[0][colonne] == 0 

    def placer_jeton(self, colonne):
        """ Joue le coup du joueur dans la colonne choisie.
        Si la colonne n'est pas disponible il faut choir une autre colonne
        """
        self.tableJeu[self.ligne][colonne] == self.joueur

    def verifier_victoire(self, ligne, colonne):
        """ vérifie si le dernier coup joué, qui a placé le jeton
        de joueur en (ligne,colonne) permet de gagner, on devra 
        tester toutes les combinaisons possibles : colonne, ligne
        et diagonales
        """
        #vérifier si la ligne est correcte
        l, c = ligne, colonne
        pionsColonne = 0
        while c > 0 and self.tableJeu[l][c-1] == self.joueur:
            pionsColonne += 1
            c = c - 1
        c = colonne 
        while c < 6 and self.tableJeu[l][c+1] == self.joueur:
            pionsColonne += 1
            c = c + 1
        if pionsColonne >= 4:
            return True

        #vérfier si la colonne est correcte 
        l, c = ligne, colonne
        pionsLigne = 0
        while l > 0 and self.tableJeu[l-1][c] == self.joueur:
            pionsLigne += 1
            l -= 1
        l = ligne
        while l < 5 and self.tableJeu[l+1][c] == self.joueur:
            pionsLigne += 1
            l += 1
        if pionsLigne >= 4:
            return True

        #vérifier si la diagonale haut gauche --> bas droit est correcte
        l, c = ligne, colonne
        pions1Diago = 0
        while l < 5 and c > 0 and self.tableJeu[l+1][c-1] == self.joueur:
            pions1Diago += 1
            l += 1
            c -= 1
        l,c = ligne, colonne
        while l > 0 and c < 6 and self.tableJeu[l-1][c+1] == self.joueur:
            pions1Diago += 1
            l -= 1
            c += 1
        if pions1Diago >= 4:
            return True

        #vérifier si la diagonale bas gauche --> haut droit est correcte
        l, c = ligne, colonne
        pions2Diago = 0
        while l > 0 and c > 0 and self.tableJeu[l-1][c-1] == self.joueur:
            pions2Diago += 1
            l -= 1
            c -= 1
        l, c = ligne, colonne
        while l < 5 and c < 6 and self.tableJeu[l+1][c+1] == self.joueur:
            pions2Diago += 1
            l += 1
            c += 1
            return True
        
        return False

if __name__ == "__main__":
    nc = 7
    nl = 6
    tableJeu = [['0' for i in range(nc)] for j in range(nl)]
    print(tableJeu)
