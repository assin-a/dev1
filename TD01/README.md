Le début du TD sert à apprendre à utiliser python en mode intéractif. 
On peut faire ca grâce a une interface graphique comme git bash ou directement en installant l'interface graphique de python.



Au début du td, on évalue des expréssions,
-Expressions à évaluer sur l'interface graphique python sur vscode:

456-723,    fonctionne comme en math
4/3,        fonctionne comme en math

4/0,    python nous donne une erreur:             'ZeroDivisionError': division by zero

len('Bonjour'), Afficher la longeur de la chaîne de caractère 'Bonjour'.

'Bonjour'*5, répète la chaîne de caractère 'Bonjour'  5fois de suite

Bonjour*5, Provoque une erreur, python n'a aucune idée de ce qu'est Bonjour 

10==5,     Retourne la valeur de vérité de la comparaison entre 10 et 5, vu qu'ils ne sont pas équivalents la v.v est fausse

523 > 500     Même chose, ici la v.v retournée est vraie. 

523 >         Provoque une erreur de syntaxe, python ne sait pas ce qu'il doit comparer à 523.



La suite du td aborde les différents opérateurs arithmétiques,

*  '+'  l'addition
*  '-'  la soustraction
*  '*'  la multiplication
*  '**' l'exposant
*  '/'  la division 
*  '//' la division entière
*  '%'  le reste de la division entière


Q1.L’aire du cercle:
Utilisez une expression Python pour calculer l’aire d’un cercle de 6.5 centimètre de rayon .
        (aire) A = πr2,
                expression: 3.14*6.5**2


Q2.Secondes en minutes
Combien de minutes sont contenues dans 567734 secondes? Affichez la réponse à l’écran
au moyen d’une expression Python.
        expression: 567734//60


Pour manipuler des chaînes de caractère en python, il faut toujours les mettres entre guillemets simples ou doubles '/"


Exercice de manipulation de chaînes de caractère:

len('Bonjour'), affiche la longeur de la chaîne de caractère 'Bonjour'

'EN MAJUSCULES'.lower(),  affiche la chaîne de caractère 'EN MAJUSCULE' en minuscule (lowercase)

'Bonjour ' + 'tout le monde', Concatène les deux chaînes de caractère 'Bonjour ' et 'tout le monde'


'Haha'*10 + '!', Répète la chaîne de caractère Haha dix fois puis ajoute un point d'exclamation apres 


On voit désormais ce que sont les listes de données, une liste suit la forme suivante:

liste_1 = [1,2,3,56]

On commence par nommer notre liste, ici liste_1, on donne ensuite les éléments de la liste entre crochets, et séparés par des virgules. Les éléments d'une liste peuvent être de n'importe quel type, y compris d'autres listes.

On peut manipuler les listes comme les chaîne de caractères, 

liste_1.append(10), ajoute 10 à la fin de la liste

liste_1.extend([5,2,8]), ajoute la liste donnée à la fin de la liste

sorted(liste_1), renvoie une version triée de la liste par ordre croissant

len(liste_1),   renvoie le nombre d'éléments de la liste

max(liste_1),   renvoie le plus grand élément de la liste


Il existe plusieurs type de données, pour en connaître la valeur d'une donnée on utilise l'expression:                  type(valeur)