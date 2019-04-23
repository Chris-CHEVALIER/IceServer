UTILISATION :

Installer les dépendances node :
	$ cd Client
	$ npm i

Compiler les sources :
	$ make

Lancer le server :
	$ make server

Lancer le client (dans un autre terminal) :
	$ node Client/Client.js

TRAVAIL RÉALISÉ :

Dans le cadre des travaux pratiques de Middleware, j'ai été amené à mettre en place un serveur Ice.

Pour cela, j'ai d'abord implémenté une interface slice permettant de gérer
les données de la classe "Track" contenant, elle-même, les champs nécessaires
à la gestion de musiques (artiste, album, nom de la musique, etc.).

L'interface slice permet donc de déclarer plusieurs méthodes utiles et répondant au principe de CRUD comme l'ajout,
la suppression ou encore la recherche d'une musique.

Afin de bénéficier d'un semblant d'interface visuelle, j'ai également mis en place un
client proposant un menu à travers duquel on peut choisir de faire telle ou telle action (CRUD).

DIFFICULTÉS RENCONTRÉES :

Lors du développement de cette application, il a d'abord était question de découvrir Ice
à travers sa documentation. C'est cette étape qui m'a parut la plus compliquée à mettre
en place malgré la documentation détaillée et solide de Zero C.

J'ai eu besoin d'aide au moment de me lancer dans l'implémentation des méthodes précédemment déclarées
dans l'interface slice car je ne comprenais dans quel fichier généré par les commandes
Ice je devais les implémenter.

PERSPECTIVES D'AMÉLIORATION DU PROJET :

Afin d'améliorer ce bien maigre projet on pourrait aisément imaginer de nouvelles
classes permettant d'étendre le partage de musiques à plusieurs utilisateurs.

Ainsi, nous aurions une classe "Compte" (Identifiant, Nom, Prénom, Mot de passe, Adresse mail)
et, pourquoi pas, une classe "Playlist" (Créateur, List<Track>, Nom, Date de création) pour aller plus loin !

Enfin, nous aurions besoin d'une nouvelle interface slice permettant de gérer l'authentification d'un compte.

Voici un exemple d'implémentation de cette interface :

module AppServer {
class Track {
   		string id;
   		string nom;
   		string prenom;
   		string username;
   		string password;
        string mail;
};
interface Compte {
       	void add(Compte c);
        Compte patch(Compte c);
       	void remove(string s);
        Compte search(string s);
       	bool authentification(Compte c);
  	};
};

Pour avoir une plus large idée de la forme que pourrait avoir le système amélioré, vous trouverez
dans le répertoire courant un dossier "Schémas" dans lequel se trouve :
- un schéma de l'architure du système imaginé,
- le diagramme de séquence correspondant,
- un schéma réprésentant la communication client/serveur avec le firewall "Glacier2" qui représente également une
opportunité d'amélioration du système.