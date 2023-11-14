import pygame
import numpy as np

# Dimensions de la grille
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 40, 40

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialisation de la grille
grid = np.zeros((ROWS, COLS))

# Fonction pour mettre à jour la grille selon les règles du Jeu de la Vie
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(1, ROWS):
        for j in range(1, COLS):
            total_neighbors = np.sum(grid[i-1:i+2, j-1:j+2]) - grid[i, j]
            if grid[i, j] == 1:
                if total_neighbors < 2 or total_neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if total_neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

################# INITIALISATION DEBUT ###########################

# Initialisation de la grille avec quelques cellules vivantes
# grid = np.zeros((ROWS, COLS))
# grid[2, 3:6] = 1
# grid[4, 2:5] = 1
# grid[5, 4] = 1

# Initialisation de la grille avec quelques cellules vivantes au hasard
grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.7, 0.3])

################# INITIALISATION FIN #############################