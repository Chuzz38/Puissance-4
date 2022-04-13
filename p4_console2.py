from p4_game2 import *

class P4_console:
    def __init__(self, nl=6, nc = 7):
        self.nl = nl
        self.nc = nc
        self.nbTours = 0
        self.game = P4_game(nl, nc)

    def quiJoue(self):
        return self.game.joueur_suivant()

    def jouerTour(self):
        """
        Fonction qui fait jouer le tour du joueur
        """
        while True: # tant que le joueur n'a pas joué correctement
            print("Choisissez la colonne où vous voulez jouer.")
            print("Les colonnes allant de 0 pour la colonne à gauche et 6 pour tout à droite")
            print(" ")
            nc = input()
 
            if not self.game.placement_possible(int(nc)):
                print("Vous ne pouvez pas placer votre jeton ici, la colonne est pleine")
            else:
                self.game.placer_jeton(int(nc))
                return int(nc)

    def afficheTableau(self):
        """
        Méthode qui permet d'afficher la table de jeu
        après chaque modification pour pouvoir suivre le
        jeu en direct.
        """
        for l in range (self.nl):
            for c in range (self.nc):
                if self.game.get_case(l,c) == '0':
                    print('.', end = " ")
                elif self.game.get_case(l,c) == '1':
                    print('@', end = " ")
                else:
                    print('X', end = " ")
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
gagne = False

while not gagne and nbTours != 42:
    console.afficheTableau()
    print(" ")
    if console.game.joueur == 1:
        print(f"\n{joueur1}, c'est ton tour\n")
    else:
        print(f"\n{joueur2}, c'est à ton tour\n")
    nc = console.jouerTour()
    nl = console.game.get_ligne(nc)
    gagne = console.game.verifier_victoire(nl, nc)
    joueur = console.game.joueur_suivant()
    nbTours += 1

console.afficheTableau()
console.game.joueur_suivant()
if nbTours == 42:
    print("Vous avez fait match nul, bravo à vous 2 !")
    print("C'était une belle partie !")
elif console.game.joueur == 1:
    print(f"\nBien joué {joueur1}, vous avez gagné la partie !\n")
elif console.game.joueur == 2:
    print(f"\nBien joué {joueur2}, vous avez gagné la partie !\n")

"""Les problèmes à résoudre :
    -Si autre chose est donné au lieu d'un chiffre lors de la colonne
    pouvoir redemander un choix
    """