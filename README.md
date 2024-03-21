
## Apercu du projet



## Objectifs :dart: :bulb:
1. Collecter les statistiques des resultats matchs des 5 grands championnats d'Europe.
	- Premier League
	- Seria A Italienne
	- la Liga Espagnole
	- Bundesliga Allemande
	- La Ligue 1 Francaise

> [!NOTE]
> On retrouvera dans les statistiques: le score, le nombre de tirs(cadres/non cadres),
> le total corners, le nombre de faute, les cartons distribues, le score a la mi-temps.
> La Source actuelle ne fournit pas le nom des joueurs buteurs, ni la composition des equipes.

2. Nettoyer, traiter et exporter les donnees sur le warehouse. 

3. Analyser la data avec la requetage SQL. L'analyse se fera des interrogations les plus simples
	- Basic
		- Le score final, score a la mi-temps
		- Le nombre de fautes commises par equipe, ...
	- Medium
		- Ressortir le championnat le plus prolifique(plus de buts inscrits)
		- Les pires humiliations (defaite a domicile sur score fleuve < 5 buts)
		- Les ratios tirs/buts
	- Hard
	 	- Surprenant mais ressortir le classement par saison. Tout simplement par ce que le jeu de donnees
	   	ne traite que le resultat score. On doit refaire le parcours pour determiner 
	   	l'equipe champion et le classement general 
		- Les statistiques approfondies par ligue, par equipe, par saison.

> [!IMPORTANT]
> Le choix de faire appel le moins possible a des bibliotheques externes est volontaire.
> Cela ne dit pas qu'on doute de la confiance à des ressources reputées de la communaute.
> Ce choix est guidé dans un but d'apprentissage et de mise en pratique des compétences en CS et problems solving.




## Stack Technologique :desktop_computer:
* Python 3.x : Extraction Traitement et chargement des donnees sur la Base
* MySQL / MariaDB : Base de donnees relationnelle pour le stockage des donnees
* SQL : Pour requeter sur les donnees.


## Structuration du projet
TopLeague/ (Repertoire principal du projet)
   |
   |---- LICENSE
   |
   |---- README
   |
   |---- scripts/
   |       |
   |       |---- config/
   |       |       |
   |       |       |---- config.ini 
   |       |
   |       |---- extraction.py


## Utilisation
1. Cloner le projet
```
git clone https://github.com/bylaye/TopLeague.git
```

2. Installer les dependances 
```
pip install -r requirements.txt
```


## Contribution
Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet en ajoutant de nouvelles fonctionnalités, en améliorant l'analyse des données ou en corrigeant des erreurs, n'hésitez pas à ouvrir une Pull Request.

