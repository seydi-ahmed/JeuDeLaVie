# Jeu de la Vie - John Conway

## Description:
Une implémentation simple du Jeu de la Vie de Conway en utilisant Python et Pygame.

## Règles du Jeu de la Vie:
Le Jeu de la Vie est un automate cellulaire créé par le mathématicien John Conway. Il se déroule sur une grille bidimensionnelle infinie et évolue au fil du temps en fonction d'un ensemble de règles simples. Les règles sont les suivantes :

1. **Survie:** Une cellule vivante avec 2 ou 3 voisins vivants survit.
2. **Naissance:** Une cellule morte avec exactement 3 voisins vivants devient une cellule vivante.
3. **Mort:** Une cellule vivante avec moins de 2 voisins vivants meurt d'isolement, et avec plus de 3 voisins vivants meurt de surpopulation.

## Comment Jouer:
- **Cloner le repertoire:** `git clone https://github.com/seydi-ahmed/JeuDeLaVie.git`.
- **Logiciels:** Assurez-vous d'installer Python et Pygame sur votre machine.
- **Lancer le Jeu:** Exécutez le script Python avec `python3 game.py`.
- **Pause:** Appuyez sur la barre d'espace pour mettre en pause ou reprendre le jeu.
- **Accélérer ou ralentir:** Allez à la ligne 81 qui contient "clock.tick(5)". Selon vos goûts, augmentez le "5" si le jeu est lent, diminuez au cas contraire.
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


## Développeur:
- **Prénom Nom:** Mouhamed Diouf
- **Ecole:** Zone01 Dakar
- **Email:** seydiahmedelcheikh@gmail.com
- **Numéro de téléphone:** +221776221681
- **LinkedIn:** https://www.linkedin.com/in/mouhamed-diouf-435207174/