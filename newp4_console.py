from p4_game import *
import random

class P4_console:
    def __init__(self, nl=6, nc = 7):
        self.nl = nl
        self.nc = nc
        self.nbTours = 0
        self.game = P4_game(nl, nc)

    def quiJoue(self):
        """
        Méthode qui permet de nous donner, quel
        joueur doit jouer.
        """ 
        pass # donne le tour du joueur 1 ou 2 

    def jouerTour(self):
        """
        Fonction qui fait joueur le tour au joueur
        """
        while True: # tant que le joueur n'a pas joué correctement
            print("Choisissez la colonne où vous voulez jouer.")
            print(" ")
            nc = int(input())

            if not self.game.placement_possible(nc):
                print("Vous ne pouvez pas placer votre jeton ici")
            else:
                self.game.placer_jeton(nc)
                return self.game.placer_jeton(nc)

    def afficheTableau(self):
        """
        Méthode qui permet d'afficher la table de jeu
        après chaque modification pour pouvoir suivre le 
        jeu en direct.
        """
        for l in range (self.nl):
            for c in range (self.nc):
                print(self.game.get_case(l,c), end = " ")
            print()

console = P4_console()

print()
print("Vous allez jouer au jeu du puissance 4")
print("Pour gagner une partie de puissance 4, il suffit d'être le premier à") 
print("aligner 4 de vos jetons soit horizontalement,")
print("soit verticalement ou même diagonalement. Si lors d'une partie,")
print("toutes les cases ont été joués sans qu'il n'y ait,")
print("de vainqueur, le match nul sera alors déclaré.")
print()


"""Il faut définir joueur avant de commencer le jeu"""
print("Joueur n°1, donnez votre nom :")
joueur1 = input()
print("Joueur n°2, donnez votre nom :")
joueur2 = input()
nc = 0
nl = 0
nbTours = 0

while not console.game.verifier_victoire(nl, nc) or nbTours == 42:
    console.afficheTableau()
    print(" ")
    if console.game.joueur == 1:
        print(f"\n{joueur1},c'est ton tour\n")
    else:
        print(f"\n{joueur2},c'est à ton tour\n")
    nl = console.jouerTour()
    print(nl)
    joueur = console.game.joueur_suivant()
    nbTours += 1
    """
    nl = console.game.get_ligne(nc) #
    
    nl = console.game.placer_jeton(nc) - 1
    print(nl)"""
    

console.game.joueur_suivant()
if console.game.joueur == 1:
    print(f"\nBien joué {joueur1}, vous avez gagné la partie !\n")
elif console.game.joueur == 2:
    print(f"\nBien joué {joueur2}, vous avez gagné la partie !\n")
elif nbTours == 42:
    print("Vous avez fait match nul, bravo à vous 2 !")
    print("Cétait une belle partie !")

"""Les problèmes à résoudre :
    -Si autre chose est donné au lieu d'un chiffre lors de la colonne
    pouvoir redemander un choix
    -"""