# Master 1 Génétique | Chef du projet: Chebab Nesrine|Lien du dépôt GitHub:
https://github.com/gene-chebab/ADN-Sequence-Analysis
# Date : 08/12/2025
# - Chebab Nesrine 
# - Tahir Fatima Zahra 
# - Radjai kamilia
# - Bouaricha siham

# 1) créer et afficher le tableau 
import pandas as pd 
data = { "Séquence": [
        "ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA",
        "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT" ],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]}

df = pd.DataFrame(data)

# 2) اSélectionner et afficher la colonne de Longueur
print(df["Longueur"].
      
print("Question 3 : sélectionner les séquences dont la longueur est > 10")
seq_gt_10 = df[df["Longueur"] > 10]
print("Séquences > 10 :")
print(seq_gt_10)

print("Question 4 : calculer la moyenne du %GC avec 3 chiffres après la virgule")
moy_gc = df["Pourcentage_GC"].mean()
moy_gc = round(moy_gc, 3)
print("Moyenne GC :", moy_gc)
import pandas as pd
# Tableau des séquences ADN sequences = [ "ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT" ] 
# Création du DataFrame 
df = pd.DataFrame({"Séquence": sequences}) 
# Calcul de la longueur de chaque séquence 
df["Longueur"] = df["Séquence"].str.len()
# Calcul du pourcentage de GC avec 3 chiffres après la virgule
df["%GC"] = ((df["Séquence"].str.count("G") + df["Séquence"].str.count("C")) / df["Longueur"] * 100).round(3) 
# QUESTION 5 : Ajouter la colonne "Catégorie GC" def categorie_gc(pourcentage): if pourcentage > 55: return "Riche" elif 45 <= pourcentage <= 55: return "Moyen" else: return "Faible"
df["Catégorie GC"] = df["%GC"].apply(categorie_gc)--
# QUESTION 6 : Ajouter une colonne comptant le nombre de 'G' 
#df["Nombre_G"] = df["Séquence"].str.count("G") 
