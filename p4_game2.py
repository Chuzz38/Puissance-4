"""
On va créer une classe puissance 4 qui aura les différents attributs
et les différentes méthodes pour rendre le puissance 4 possible
"""

class P4_game:
    def __init__(self, nl=6, nc=7):
        self.nl = nl
        self.nc = nc
        self.joueur = 1
        self.tableJeu = [['0' for i in range(nc)] for j in range(nl)]

    def get_case(self, ligne, colonne):
        """
        Prend en paramètres la ligne et la colonne
        et renvoie ce qu'il y a dans cette case
        """
        return self.tableJeu[ligne][colonne]

    def get_ligne(self, colonne):
        """
        Fonction qui renvoie la ligne par rapport
        à la colonne qui vient d'être joué. Soit la
        plus haute ligne avec un jeton
        """
        ligne = 0
        while ligne < self.nl and self.tableJeu[ligne][colonne] == '0':
            ligne += 1
        return ligne

    def joueur_suivant(self):
        """
        Cette fonction permet de passer au joueur suivant
        """
        self.joueur %= 2
        self.joueur += 1

    def placement_possible(self, colonne):
        """
        Prend en parametre seulement la colonne et renvoie
        True si la colonne est jouable et False sinon
        """
        return self.tableJeu[0][colonne] == '0'

    def placer_jeton(self, colonne):
        """
        Joue le coup du joueur dans la colonne choisie.
        On suppose que placement est possible
        """
        vide = 0
        while vide < self.nl and self.tableJeu[vide][colonne] == '0':
            vide += 1

        if self.joueur == 1:
            self.tableJeu[vide-1][colonne] = '1'
        else:
            self.tableJeu[vide-1][colonne] = '2'

        return vide

    def verifier_victoire(self, ligne, colonne):
        """
        Vérifie si le dernier coup joué par le joueur
        permet de gagner. On devra tester toutes les 
        combinaisons possibles : colonne, ligne
        et diagonales.
        """
        # Vérifier si la ligne est gagnée
        if self.joueur == 1:
            jeton = '1'
        else:
            jeton = '2'
        l, c = ligne, colonne
        pionsTotal = 1
        while c > 0 and self.tableJeu[l][c-1] == jeton:
            pionsTotal += 1
            c -= 1
        c = colonne
        while c < 6 and self.tableJeu[l][c+1] == jeton:
            pionsTotal += 1
            c += 1
        if pionsTotal >= 4:
            return True

        # Vérfier si la colonne est gagnée
        l, c = ligne, colonne
        pionsTotal = 1
        while l > 0 and self.tableJeu[l-1][c] == jeton:
            pionsTotal += 1
            l -= 1
        l = ligne
        while l < 5 and self.tableJeu[l+1][c] == jeton:
            pionsTotal += 1
            l += 1
        if pionsTotal >= 4:
            return True

        # Vérifier si la diagonale haut gauche --> bas droit est gagnée
        l, c = ligne, colonne
        pionsTotal = 1
        while l < 5 and c > 0 and self.tableJeu[l+1][c-1] == jeton:
            pionsTotal += 1
            l += 1
            c -= 1
        l,c = ligne, colonne
        while l > 0 and c < 6 and self.tableJeu[l-1][c+1] == jeton:
            pionsTotal += 1
            l -= 1
            c += 1
        if pionsTotal >= 4:
            return True

        # Vérifier si la diagonale bas gauche --> haut droit est gagnée
        l, c = ligne, colonne
        pionsTotal = 1
        while l > 0 and c > 0 and self.tableJeu[l-1][c-1] == jeton:
            pionsTotal += 1
            l -= 1
            c -= 1
        l, c = ligne, colonne
        while l < 5 and c < 6 and self.tableJeu[l+1][c+1] == jeton:
            pionsTotal += 1
            l += 1
            c += 1
        if pionsTotal >= 4:
            return True
        
        return False

if __name__ == "__main__":
    nc = 7
    nl = 6
    tableJeu = [['.' for i in range(nc)] for j in range(nl)]
    print(tableJeu)