import pygame
import numpy as np
import time
from tours import *

# Dimensions de la grille
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 40, 40

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

########################### INITIALISATION DEBUT ###########################

# Initialisation de la grille avec quelques cellules vivantes manuellement
# grid = np.zeros((ROWS, COLS))
# grid[2, 3:6] = 1
# grid[4, 2:5] = 1
# grid[5, 4] = 1

# Utilisez une des fonctions d'initialisation du module tours
# grid = np.zeros((ROWS, COLS))

# Initialisation de la grille avec quelques cellules vivantes au hasard
grid = random_grid()

########################### INITIALISATION FIN #############################

# Fonction pour mettre à jour la grille selon les règles du Jeu de la Vie
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
            total_neighbors = np.sum(grid[i-1:i+2, j-1:j+2]) - grid[i, j]
            if grid[i, j] == 1:
                if total_neighbors < 2 or total_neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if total_neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

# Fonction principale pour exécuter le Jeu de la Vie
def run_game():
    global grid
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jeu de la Vie - John Conway")

    clock = pygame.time.Clock()

    running = True
    paused = True  # Démarrez en mode pause
    mouse_pressed = False

    while running:
        window.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pressed = False

        if not paused:
            grid = update_grid(grid)

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

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    run_game()
