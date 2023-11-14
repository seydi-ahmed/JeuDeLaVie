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