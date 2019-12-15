**MacGyver-Game**
[P3] - OpenClassRoom Développeur Python - 

Création d'un jeu de logique (labyrinthe) en Python 3, orienté objets
dont le but est d'emmener le héros (MacGyver) à quitter le labyrinthe avec succès.
Description:

- 5 Niveaux sont accompagnés de fond sonore
- Gestion du temps

Pré - Requis
Python 3 et la librairie Pygame est indispensable au bon fonctionnement du programme.

Vous pouvez installer python3 à l'adresse suivante : https://www.python.org/downloads/

Pour le module Pygame, vous devez déjà avoir pip installé sur votre machine. Lancez l'installation de pygame avec cette commande dans votre terminal :

**python3 -m pip install -U pygame --user**

Lancement du jeu
Après avoir installé python 3 et pygame, vous devez lancer le jeu depuis votre terminal avec la commande suivante :

**python3 main.py**

Gameplay : 
Le personnage se déplace à l'aide des flèches directionnelles du clavier et uniquement des fléches (pour l'instant, aucune autre combinaison de touche ou l'utilisation de la souris ne sont implémantés).

Votre héros devra se frayer un chemin sur un chemin, entouré de hauts murs infranchissables. A vous donc de le faire se mouvoir, sans pouvoir franchir les murs, trop hauts pour lui.

Afin d'endormir le gardien, votre héros devra absolument rassembler trois objets indispensables : une aiguille, un tuyau en PVC et une bouteille d'éther. Gare à vous si vous vous retrouvez devant votre ennemi sans ses trois objets : vous péririez dans d'atroces souffrances !

Un compteur est situé en haut au milieu droite de l'écran pour vous aider à voir combien d'objets vous avez déjà ramassé.
Une gestion de temps pour coanniatre si vous avez été le plus rapide a sortir des 5 niveaux

Touches utiles :
 - Flèches directionnelles : déplacement du personnage
 - 'F1' : Lancer le jeu
 - 'Echap' : fermeture de la fenêtre