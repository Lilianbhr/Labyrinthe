# Labyrinthe Dynamique (Architecture Modulaire)

Ce projet est un jeu d'exploration développé en Python avec Pygame. Il se distingue par une séparation stricte entre la logique métier, les constantes de configuration et les données de niveau.

## Architecture du Projet

Le code est structuré de manière modulaire pour favoriser la maintenabilité :
- **`main.py`** : Point d'entrée, gestion de la boucle de jeu et parsing du niveau.
- **`classes.py`** : Définition des entités (POO) et de la logique de collision.
- **`generale.py`** : Centralisation des constantes (dimensions, couleurs, groupes de sprites).
- **`labyrinthe.txt`** : Matrice de données définissant la structure du niveau.

## Fonctionnalités Techniques

- **Parsing de niveau** : Algorithme de lecture de fichier ligne par ligne pour instancier les sprites de murs aux coordonnées $(x, y)$ correspondantes.
- **Système de Brouillard (Masque)** : Implémentation d'un calque dynamique qui suit le joueur, limitant son champ de vision pour renforcer l'aspect exploration.
- **Gestion du Temps Précise** : Utilisation de la classe `datetime` et `timedelta` pour créer un chronomètre qui s'arrête une fois l'objectif atteint (5 confitures récoltées).
- **Logique de Collision Prédictive** : Le joueur enregistre sa position précédente avant chaque mouvement ; en cas de collision avec un mur, il subit un "rollback" vers ses anciennes coordonnées.

## Notions Informatiques Valorisées

- **Héritage et POO** : Utilisation intensive de la classe `pygame.sprite.Sprite`.
- **Manipulation de Flux (I/O)** : Ouverture et lecture de fichiers externes (`open()`, `readlines()`).
- **Algorithmes de Grille** : Transformation d'une matrice texte de $21 \times 21$ en un rendu graphique pixelisé cohérent.

## Installation
1. Installez Pygame : `pip install pygame`
2. Lancez le jeu : `python main.py`
