import Alen_P4
import pygame
import sys
import p4_game



def chargement():
    ''' Cette fonction affiche l'interface graphique du jeu de puissance 4. '''
    global fenetre, pionR, pionJ
    pygame.init()
    fenetre = pygame.display.set_mode((700,600))

    pionR = pygame.image.load(sys.path[0] + "/pr.png").convert()
    pionJ = pygame.image.load(sys.path[0] + "/pj.png").convert()

    pygame.display.flip()

def affichage_plateau():
    ''' Cette fonction affiche le plateau vide.
        La fonction chargement_jeu() doit avoir été appelée avant. '''
    global fond
    fond = pygame.image.load(sys.path[0] + "/grille.png")

    fenetre.blit(fond, (0,0))
    pygame.display.flip()

def affichage_pion():
    ''' Cette fonction dessine le pion du joueur donné à la position donnée.
        Le paramètre joueur doit avoir la valeur 1 pour les pions rouges.    '''
    if joueur == 1:
        pion = pionR
    else:
        pion = pionJ

    while event.type == MOUSEBUTTONDOWN: 
        if event.pos >= (0,0) and event.pos <= (100,600):
            colonne = 1
        if event.pos >= (100,0) and event.pos <= (200,600):
            colonne = 2
        if event.pos >= (200,0) and event.pos <= (300,600):
            colonne = 3
        if event.pos >= (300,0) and event.pos <= (400,600):
            colonne = 4
        if event.pos >= (400,0) and event.pos <= (500,600):
            colonne = 5
        if event.pos >= (500,0) and event.pos <= (600,600):
            colonne = 6
        if event.pos >= (600,0) and event.pos <= (700,600):
            colonne = 7

    
    fond.blit(pion,(num_colonne,num_ligne))

    fenetre.blit(fond, (0,0))
    pygame.display.flip()

### test juste en bas là 

if __name__ == "__main__":
    while not verifier_victoire:
        print(chargement())
        print(affichage_plateau())
    
    
# screen.blit(jetonRouge, (16 + 97 * colonne, 13 - 97.5 * lignedejeu + 486))