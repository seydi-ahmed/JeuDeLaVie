import pygame
import numpy as np
import time
from tours import *

# Dimensions de la grille
WIDTH, HEIGHT = 800, 800 # la taille de la grille principale
ROWS, COLS = 40, 40 # les cellules à l'intérieur

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

########################### INITIALISATION DEBUT ###########################

# Utilisez une initialisation en commentant les deux autres
# donner 1 à une cellule veut dire qu'elle est vivante
# donner 0 à une cellule veut dire qu'elle est morte

# Initialisation de la grille avec quelques cellules vivantes manuellement
# grid = np.zeros((ROWS, COLS))
# grid[2, 3:6] = 1
# grid[4, 2:5] = 1
# grid[5, 4] = 1

# Initialisation avec zéro case noire. A vous de définir votre début de jeu
# grid = np.zeros((ROWS, COLS))

# Initialisation de la grille avec quelques cellules vivantes au hasard
grid = random_grid()

########################### INITIALISATION FIN #############################

# Fonction pour mettre à jour la grille selon les règles du Jeu de la Vie
def update_grid(grid):
    new_grid = grid.copy() # Copier la grille pour ne pas toucher à celle du jeu
    for i in range(ROWS): # Parcourir les lignes
        for j in range(COLS): # Parcourir les colonnes
            voisins = np.sum(grid[i-1:i+2, j-1:j+2]) - grid[i, j] # Stocker les voisins en excluant la cellule elle-même
            if grid[i, j] == 1: # Cellule vivante avec moins de 2 ou plus de 3 voisins meurent
                if voisins < 2 or voisins > 3:
                    new_grid[i, j] = 0
            else: # Cellule morte avec 3 voisins prend vie
                if voisins == 3:
                    new_grid[i, j] = 1
    return new_grid

# Fonction principale pour exécuter le Jeu de la Vie
def run_game():
    # Déclarer la variable globale "grid"
    global grid 
    
    # Initialiser le module pygame
    pygame.init() 

    # Créer une fenêtre graphique avec une largeur augmentée de 200 pixels
    window = pygame.display.set_mode((WIDTH + 200, HEIGHT)) 

    # Définir le titre de la fenêtre
    pygame.display.set_caption("Jeu de la Vie - John Conway")

    # Créer un objet Clock pour contrôler la vitesse du jeu
    clock = pygame.time.Clock()

    # Créer un objet Font pour afficher du texte avec une taille de police de 36
    font = pygame.font.Font(None, 36)

    # Initialiser la variable qui stocke le moment où le timer a commencé
    timer_start = None

    # Initialiser la variable qui stocke le temps écoulé pendant les pauses
    paused_time = 0

    # Initialiser la variable qui compte le nombre de générations
    generations = 0

    # Initialiser la variable qui contrôle si le jeu est en cours d'exécution
    running = True

    # Initialiser la variable qui contrôle si le jeu est en pause
    paused = True

    # Initialiser la variable qui contrôle si le bouton de la souris est enfoncé
    mouse_pressed = False

    # Boucle principale du jeu
    while running:
        # Remplit la fenêtre avec la couleur blanche
        window.fill(WHITE)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Gestion de la touche Espace pour mettre en pause ou reprendre le jeu
                if event.key == pygame.K_SPACE:
                    if paused:
                        # Si le jeu est en pause, enregistre le moment de la reprise
                        timer_start = time.time() - paused_time
                    else:
                        # Si le jeu reprend, enregistre le temps écoulé pendant la pause
                        paused_time = time.time() - timer_start
                    # Inverse l'état de la pause
                    paused = not paused

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Gestion du clic de la souris pour changer l'état des cellules
                mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pressed = False

        # Met à jour la grille si le jeu n'est pas en pause
        if not paused:
            grid = update_grid(grid)
            generations += 1

        # Gestion du clic de la souris pour changer l'état des cellules
        if mouse_pressed:
            x, y = pygame.mouse.get_pos()
            col = x // (WIDTH // COLS)
            row = y // (HEIGHT // ROWS)
            grid[row, col] = 1

        # Dessin de la grille
        for i in range(ROWS):
            for j in range(COLS):
                color = BLACK if grid[i, j] == 1 else WHITE
                rect = pygame.Rect(j * (WIDTH // COLS), i * (HEIGHT // ROWS), WIDTH // COLS, HEIGHT // ROWS)
                pygame.draw.rect(window, color, rect)

                # Dessine des lignes de séparation verticales
                pygame.draw.line(window, BLACK, (j * (WIDTH // COLS), 0), (j * (WIDTH // COLS), HEIGHT), 1)

                # Dessine des lignes de séparation horizontales
                pygame.draw.line(window, BLACK, (0, i * (HEIGHT // ROWS)), (WIDTH, i * (HEIGHT // ROWS)), 1)

        # Dessiner le rectangle à l'extérieur de la grille
        pygame.draw.rect(window, GRAY, (WIDTH, 0, 1000, HEIGHT))

        # Afficher le timer
        if timer_start is not None:
            elapsed_time = int(time.time() - timer_start) if not paused else int(paused_time)
        else:
            elapsed_time = int(paused_time)
        timer_text = font.render(f"T: {elapsed_time}s", True, BLACK)
        window.blit(timer_text, (WIDTH + 10, 10))

        # Afficher le nombre de générations
        generation_text = font.render(f"G: {generations}", True, BLACK)
        window.blit(generation_text, (WIDTH + 10, 50))

        # Afficher la légende de T et de G
        generation_text = font.render(f"LEGENDE", True, BLACK)
        window.blit(generation_text, (WIDTH + 40, 100))
        generation_text = font.render(f"T = Temps", True, BLACK)
        window.blit(generation_text, (WIDTH + 10, 140))
        generation_text = font.render(f"G = Générations", True, BLACK)
        window.blit(generation_text, (WIDTH + 10, 180))

        # Met à jour l'affichage
        pygame.display.flip()
        # Contrôle la vitesse du jeu
        clock.tick(5)

    # Quitte le jeu lorsque la boucle se termine
    pygame.quit()

if __name__ == "__main__":
    run_game()
