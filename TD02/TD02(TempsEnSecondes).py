# Script qui demande un nombre d’heures, un nombre de minutes et un nombre
# de secondes et qui affiche le nombre de secondes totales

h = int(input("Entrez le nombre d'heures entières: "))
m = int(input("Entrez le nombre de minutes entières: "))
s = int(input("Entrez le nombre de secondes entières: "))



print("Le nombre de secondes totales est de:", h*3600 + m*60 +s, "secondes")
