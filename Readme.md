# Jeu de la Vie - John Conway

## Description:
Une implémentation simple du "Jeu de la Vie" de John Conway en utilisant Python et Pygame.

## Règles du Jeu de la Vie:
Le Jeu de la Vie est un automate cellulaire créé par le mathématicien John Conway. Il se déroule sur une grille bidimensionnelle infinie et évolue au fil du temps en fonction d'un ensemble de règles simples. Les règles sont les suivantes :

1. **Survie:** Une cellule vivante avec 2 ou 3 voisins vivants survit.
2. **Naissance:** Une cellule morte avec exactement 3 voisins vivants devient une cellule vivante.
3. **Mort:** Une cellule vivante avec moins de 2 voisins vivants meurt d'isolement, et avec plus de 3 voisins vivants meurt de surpopulation.

## Comment Jouer:
- **Cloner le repertoire:** `git clone https://github.com/seydi-ahmed/JeuDeLaVie.git`
- **Logiciels:** Assurez-vous d'installer Python et Pygame sur votre machine.
    1) Windows:
        ```
        a) Python: https://www.python.org/downloads/
        b) Pygame: pip install pygame
    2) Ubuntu:
        ```
        a) Python: les distributions de Ubuntu viennent avec python préinstallé
        Installer les dépendances:
        sudo apt-get update
        sudo apt-get install python3-dev python3-pip
        sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
        b) Pygame: pip3 install pygame
    3) Mac Os:
        ```
        a) Python: macOS est livré avec Python préinstallé
        b) Pygame: pip3 install pygame
    ```
    Veuillez noter que l'utilisation de pip3 au lieu de pip est courante pour les installations Python 3.
- **Lancer le Jeu:** Exécutez le script Python avec `python3 game.py`.
- **Jouer - Pause:** Appuyez sur la barre d'espace pour commencer, mettre en pause ou reprendre le jeu.
- **Accélérer ou ralentir:** Allez à la ligne qui contient `clock.tick(5)`qui est l'avant derniere ligne de la fonction `run_game()`. Selon vos goûts, augmentez ou diminuez le `5` pour accélerer ou ralentir le jeu.
- **Quitter:** Fermez la fenêtre du jeu.

## Configuration Initiale (commentez une des initialisations pour utiliser celle que vous voulez)
### Initialisation manuelle:
La grille est initialisée avec quelques cellules vivantes pour illustrer le fonctionnement du jeu. Vous pouvez ajuster la configuration initiale en modifiant les lignes du script Python qui définissent les cellules vivantes.
```python
grid = np.zeros((ROWS, COLS))
grid[2, 3:6] = 1
grid[4, 2:5] = 1
grid[5, 4] = 1
```

### Initialisation au hasard:
la grille est initialisée au hasard.
```python
grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.7, 0.3])
```

### Initialisation sur la grille:
La grille est composée de cellules mortes appuyez sur une case pour la mettre en noire (lui donner vie)
```python
grid = np.zeros((ROWS, COLS))
```

### Configurations:
les configurations standards se trouvent dans tours.py
```python
Block, Bee-hive, loaf, boat, Tub, Blinker(period 2), Toad(period 2), Beacon(period 2), Pulsar(period 3), Penta-decathlon(period 15), Glider, Light-weight spaceship(LWSS), Middle-weight spaceship(MWSS), Heavy-weight spaceship(HWSS), The R-pentomino, Diehard, Acorn, Gosper glider gun, Simkin glider gun.

Pour les utiliser on a juste à appeler la fonction avec "grid = <nom_de_la_fonction>"
```

### Taille de la grille:
Juste aprés avoir importé les modules à utiliser vous avez les dimensions de la grille avec:
```
WIDTH, HEIGHT = 800, 800 (la taille de la grille principale)
ROWS, COLS = 40, 40 (les cellules à l'intérieur)
```
Augmentez ou diminuez la grille selon vos préférences

## Coordonnées du développeur:
- **Prénom Nom:** Mouhamed Diouf
- **Ecole:** Zone01 Dakar
- **Email:** seydiahmedelcheikh@gmail.com
- **Numéro de téléphone:** +221776221681
- **LinkedIn:** https://www.linkedin.com/in/mouhamed-diouf-435207174/
- **Github:** https://github.com/seydi-ahmed
- **Twitter:** https://twitter.com/SeydiAhmed007

## Tutos youtube suivis:
- **ScienceEtonnante:** https://www.youtube.com/watch?v=S-W0NX97DB0&t=238s
- **Rational Animations:** https://www.youtube.com/watch?v=C2vgICfQawE
- **Numberphile:** https://www.youtube.com/watch?v=R9Plq-D1gEk