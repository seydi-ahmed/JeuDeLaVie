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

# Initialisation de la grille avec quelques cellules vivantes
grid = np.zeros((ROWS, COLS))
grid[2, 3:6] = 1
grid[4, 2:5] = 1
grid[5, 4] = 1

# Initialisation de la grille avec quelques cellules vivantes au hasard
grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.7, 0.3])