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

########################### INITIALISATION DEBUT ###########################

# Initialisation de la grille avec quelques cellules vivantes manuellement
# grid = np.zeros((ROWS, COLS))
# grid[2, 3:6] = 1
# grid[4, 2:5] = 1
# grid[5, 4] = 1

# Initialisation de la grille avec quelques cellules vivantes au hasard
grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.7, 0.3])

########################### INITIALISATION FIN #############################

# Fonction principale pour exécuter le Jeu de la Vie
def run_game():
    global grid
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jeu de la Vie - John Conway")

    clock = pygame.time.Clock()

    running = True
    paused = False

    while running:
        window.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

        if not paused:
            grid = update_grid(grid)

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
