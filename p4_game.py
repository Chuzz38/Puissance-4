import random
"""On va créer une classe puissance 4 qui aura les différents attributs
et les différentes méthodes pour rendre le puissance 4 possible"""


""". ; O ; X --> interface, affichage
0 : case vide ; 1 : case du joueur un ; 2 : case du jouer 2
pour pouvoir stocker au fur et mesure du jeu"""

"""tester à chaque fois si il y a victoire et si c'est vide on ne peut pas mettre au dessus : retourne si """

class P4_game:
    
    def __init__(self, nl=6, nc=7,jeton=('O','X')):
        self.nl = nl
        self.nc = nc
        self.jeton = jeton
        self.tableJeu = [['.' for i in range(nc)] for j in range(nl)]
        self.nouvellepartie(self.nl, self.nc, self.jeton)

    def tourJoueur(self, nbTour = 0):
        x = 0
        if self.nbTour == 0: #si la partie commence
            x = random.randint(0, 1)
            if x == 0:
                return joueur1
            else:
                return joueur2
        else:plus de '.' dans la ligne, elle est donc remplieueur1
            else:
                return joueur2

    def get_case(self, ligne, colonne):
        return self.tableJeu[ligne][colonne]


    """def jeu_possible(self, ligne, colonne):
        if self.get_case(self.ligne, self.colonne) == '.':
            return True
        else: #si la case est déja prise (O ou X)
            return False"""

    def placement_possible(self, colonne):
        """Prend en parametre seulement la colonne et renvoie 
        True si la case est libre et False sinon"""
        for i in range(ligne): #?
            if self.get_case(,)

    def placer_jeton(self, joueur, colonne):
        """ Joue le coup du joueur dans la colonne choisie.
        Retourne (False) si le coup n'est pas valide (si la colonne
        est déjà remplie)
        Retourne (True, ligne) si le coup est valide, avec ligne la ligne dans
        laquelle se trouve le jeton jouée. Si le coup est valide,
        la méthode modifie la table de jeu en cours.
        """
        if placement_possible(colonne, joueur): # == True ?
    

    def afficher_table(self, joueur, tableJeu):
        pass #montrer la table de jeu à un moment donné


    def victoire(self, ligne, colonne, joueur):
        """ vérifie si le dernier coup joué, qui a placé le jeton
        de joueur en (ligne,colonne) permet de gagner, on devra 
        tester toutes les combinaisons possibles : colonne, ligne
        et diagonales
        """
        gagné = self.jeton[joueur-1] * 4 #on donne la combinaison pour que ça soit gagné
        for i in range(ligne):
            for j in range(colonne):


    def nouvellepartie(self, nl=6, nc=7, jeton =('O', 'X'))
        pass

if __name__ == "__main__":