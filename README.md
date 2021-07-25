# Projet 11 : Améliorez un projet existant en Python

## Contexte du proojet

Marlin Guillou est un jeune entrepreneur de 37 ans à la tête de plusieurs agences immobilières qui souhaite en plus de 
son activité actuelle se lancer, dans 4 mois, dans un projet associatif solidaire : l’accompagnement des familles aux 
revenus modestes dans l’achat d’un bien immobilier. Fort de son expérience dans le domaine et de son large réseau, 
Marlin a pour idée de développer une application simple d’utilisation permettant la mise en ligne, par des agences 
immobilières, d’annonces immobilières consultables par tous. Toutefois, seuls les inscrits pourront sélectionner 
les biens encore disponibles sur lesquels ils souhaitent se positionner afin d’être contactés par l’agent immobilier 
ayant déposé l’annonce. Marlin supervisera l’application mais en laissera la gestion à Stéphane, 
le vice-président de l’association.


## Liens

* [Lien vers Trello](https://trello.com/b/Tip34mux/projet-13-projet-final-asso-app-immo)
* [Lien en ligne ](https://app-asso-immo.herokuapp.com/)

## Installation

Pour copier le projet en local, ouvrer un terminal et taper les commandes suivantes

```clone
$ git clone https://github.com/souleymanediallo/app-asso-immo.git
```

Installer un environnement virtuel
```virtualenv
$ pip install virtualenv
```

Créer un environnement virtuel
```venv
$ virtualenv venv
```

Activer l'environnement virtuel
```activate
$ source venv/bin/activate
```

Créer une base de donnée Postgresl
```basededonnee
$ createdb app_asso_immo
```

Créer un fichier .env et renseigner vos variables d'environnement
```environnement
$ touch .env
```

Intaller les dépendances du projet
```installer
$ pip install -r requirements.txt
```

Demarrer l'application avec la commande suivante

```run
$ python manage.py runserver
```

## Tests

Faire les tests

```test
python manage.py test
```

## Crée avec

* Python 3.8
* Django 3.2
* HTML5 & CSS3
* Bootstrap 5
* Start Bootstrap


## Auteur

Souleymane Diallo
Développeur Python, étudiant openclassrooms
