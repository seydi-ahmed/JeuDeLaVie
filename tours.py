import numpy as np

# Dimensions de la grille
ROWS, COLS = 40, 40

# Fonction pour initialiser la grille avec des cellules au hasard
def random_grid():
    return np.random.choice([0, 1], size=(ROWS, COLS), p=[0.7, 0.3])

# Fonction pour initialiser la grille avec la configuration "Block"
def block():
    grid = np.zeros((ROWS, COLS))
    grid[10:12, 10:12] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Beehive"
def beehive():
    grid = np.zeros((ROWS, COLS))
    grid[15:18, 15:19] = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]
    return grid

# Fonction pour initialiser la grille avec la configuration "Loaf"
def loaf():
    grid = np.zeros((ROWS, COLS))
    grid[14:18, 14:18] = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    return grid

# Fonction pour initialiser la grille avec la configuration "Boat"
def boat():
    grid = np.zeros((ROWS, COLS))
    grid[12:15, 12:15] = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    return grid

# Fonction pour initialiser la grille avec la configuration "Tub"
def tub():
    grid = np.zeros((ROWS, COLS))
    grid[15:18, 15] = 1
    grid[16, 14:16] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Blinker (période 2)"
def blinker():
    grid = np.zeros((ROWS, COLS))
    grid[15, 14:17] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Toad (période 2)"
def toad():
    grid = np.zeros((ROWS, COLS))
    grid[15:17, 14:16] = 1
    grid[16:18, 15:17] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Beacon (période 2)"
def beacon():
    grid = np.zeros((ROWS, COLS))
    grid[14:16, 14:16] = 1
    grid[16:18, 16:18] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Pulsar (période 3)"
def pulsar():
    grid = np.zeros((ROWS, COLS))
    grid[13:16, 16] = 1
    grid[13:16, 18] = 1
    grid[15, 13:16] = 1
    grid[17, 13:16] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Penta-decathlon (période 15)"
def penta_decathlon():
    grid = np.zeros((ROWS, COLS))
    grid[14, 14:16] = 1
    grid[15:17, 13] = 1
    grid[15:17, 16] = 1
    grid[15, 14:16] = 0
    return grid

# Fonction pour initialiser la grille avec la configuration "Glider"
def glider():
    grid = np.zeros((ROWS, COLS))
    grid[14, 15] = 1
    grid[15, 16] = 1
    grid[16, 14:16] = 1
    grid[16, 15] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Light-weight spaceship (LWSS)"
def lwss():
    grid = np.zeros((ROWS, COLS))
    grid[14, 15:17] = 1
    grid[15, 14] = 1
    grid[15, 17] = 1
    grid[16, 14] = 1
    grid[16, 17] = 1
    grid[17, 14:17] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Middle-weight spaceship (MWSS)"
def mwss():
    grid = np.zeros((ROWS, COLS))
    grid[14, 14:17] = 1
    grid[15, 13] = 1
    grid[15, 17] = 1
    grid[16, 13] = 1
    grid[16, 17] = 1
    grid[17, 13] = 1
    grid[17, 16] = 1
    grid[18, 13:16] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Heavy-weight spaceship (HWSS)"
def hwss():
    grid = np.zeros((ROWS, COLS))
    grid[14, 14:17] = 1
    grid[15, 13] = 1
    grid[15, 17] = 1
    grid[16, 13] = 1
    grid[16, 17] = 1
    grid[17, 13] = 1
    grid[17, 16] = 1
    grid[18, 13:15] = 1
    grid[18, 16] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "The R-pentomino"
def r_pentomino():
    grid = np.zeros((ROWS, COLS))
    grid[15, 14:16] = 1
    grid[16, 13:15] = 1
    grid[16, 15] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Diehard"
def diehard():
    grid = np.zeros((ROWS, COLS))
    grid[15, 14] = 1
    grid[16:18, 15] = 1
    grid[17, 18] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Acorn"
def acorn():
    grid = np.zeros((ROWS, COLS))
    grid[15, 14:16] = 1
    grid[16, 16] = 1
    grid[17, 13:16] = 1
    grid[17, 17] = 1
    grid[17, 18] = 1
    grid[17, 19] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Gosper glider gun"
def gosper_glider_gun():
    grid = np.zeros((ROWS, COLS))
    grid[12, 24] = 1
    grid[13, 22:24] = 1
    grid[14, 12:14] = 1
    grid[14, 16:18] = 1
    grid[14, 24] = 1
    grid[15, 12:14] = 1
    grid[15, 16:18] = 1
    grid[15, 25] = 1
    grid[16, 12:14] = 1
    grid[16, 18] = 1
    grid[16, 24] = 1
    grid[17, 13:15] = 1
    grid[17, 16] = 1
    grid[17, 22:24] = 1
    grid[18, 14] = 1
    grid[18, 16] = 1
    grid[18, 22] = 1
    grid[18, 23] = 1
    grid[19, 16] = 1
    grid[19, 22:24] = 1
    grid[20, 18] = 1
    grid[20, 19] = 1
    return grid

# Fonction pour initialiser la grille avec la configuration "Simkin glider gun"
def simkin_glider_gun():
    grid = np.zeros((ROWS, COLS))
    grid[15, 14:16] = 1
    grid[16, 13:16] = 1
    grid[17, 13] = 1
    grid[18, 14] = 1
    return grid
