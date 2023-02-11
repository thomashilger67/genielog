# Sport Tracker

Sport Tracker est l'outil parfait pour répertorier et archiver ses activités sportives.
Lorsque vous effectuer une activité sportive de type vélo, course à pied, natation ou cardio, vous avez simplement à l'ajouter à la base de données de Sport Tracker pour ne plus perdre sa trace.

Vous avez également la possibilité de modifier ou supprimer une activité déjà répertoriée. 

Le plus de Sport Tracker ? La possibilité d'avoir des statistiques sur vos performances physiques (d'autres statistiques se rajouteront avec les temps.)


 Avec son interface Web, plus besoin de coder à la main des requêtes HTTP pour afficher/ajouter/modifier/supprimer vos activités.

 ## Quistart 

 Pour lancer le webservice, vous devez posséder `Docker` et notamment `Docker compose` sur votre machine. 

 ### Installation
 Cloner le répôt Github : `git clone https://github.com/thomashilger67/genielog.git`

 ### Lancement 
 A la racine du répertoire, lancez la commande docker : `docker-compose up`

 ### Accès 
 Vous aurez accès à Sport Tracker via l'adresse suivante : `http://localhost:5000`. 
 Attention il est nécessaire que vos ports 5000 et 27017 (pour la base de données soit ouverts et libres).


 ## Documentation 

 ### Technologie utilisée
 Sport Tracker est codé en Python avec le package `flask` pour réaliser le webservice. L'ensemble est mis dans un conteneur Docker. Pour la persistance des données, on utilise une base de données NoSQL MongoDB, égalemnt mise dans un conteneur Docker. Pour l'interface web, des templates html sont utilisés. Enfin un pipeline CI/CD couplé à des test PyTest est mis en place pour garantir la fonctionnalité du code.

### Design Pattern 
4 différents types d'ativités sont supportées : vélo, course à pied, natation et cardio. Nous utilisation un design pattern de type factory pour encoder ces 4 types d'objets différents. Il y a classe abstaite Activity, de laquelle BikeActivity, RunActivity, SwimActivity et CardioActivity héritent. 

Chaque classes filles possèdent des attributs différents. Ainsi leur stockage dans une base de données relationnelles seraient peu adapté. L'utilisation de MongoDB est adéquate grâce à sa bonne gestion des documents n'ayant pas la même structure.

Auteur : Thomas Hilger (dans le cadre de l'évaluation de la matière génie logiciel)
