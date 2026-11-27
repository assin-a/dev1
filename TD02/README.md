On commence l'apprentissage de python en mode script.

Une variable fait référence à une donnée stockée en mémoire.
Par exemple, le nom d'une liste est une variable qui fait référence a la valeur stockée dans cette liste.

exemple de variables:
nom = 'Yassin'
    Ici la variable est: nom

listee = [10,12,14]
    Ici la variable est: listee

etc.

On voit ici qu'une variable peut adopter plusieurs type pour les valeurs qu'elle stocke.
Pour connaitre le type de données de chaque variable, on à recours à l'expression; type(variable)


Q1,Lancez Python en mode interactif et exécutez des instructions permettant d’arriver aux résultats demandés .
...

Q2.Expressions
Déclarez les quatre variables suivantes :
1.largeur référençant le nombre 2.8,
2.longueur référençant le nombre 34
3.texte référençant la chaîne 'le langage Python'
4.ma_liste référençant une liste contenant les chaînes'A', 'B' et 'C' (dans cet ordre)

Par la suite, il est demandé d'évaluer une série d'expréssions à l'aide de python en mode intéractif:
longeur * largeur, nous donne 34*34
largeur **3 , nous donne 2.8*2.8 (*)

max(longueur,largeur,len(texte)), retourne le max des 3 variables

texte[0:10], affiche les 10 premiers caractères de la chaîne texte.
    En python la premiere valeur d'une liste porte l'indice 0, la derniere porte l'indice n-1 où n est la longeur(len)

texte//10, provoque une erreur de type, on ne peut pas faire d'opération entre une chaîne et un entier.

texte[0]*10, répete le caractère d'indice 0 de la chaîne texte 10 fois de suite.

ma_liste+2, provoque une erreur de type, on peut concaténer une liste avec une autre liste mais pas avec un entier.


= sert à assigner une valeur à une variable,

par exemple: longueur = (5 + 3**10)/3,
ou encore    longueur = largeur
par contre, une affectation du type 5 = longeur provoque une erreur car on ne peut pas assigner une valeur à un nombre.


La suite du td aborde l'utilisation de python en mode intéractif