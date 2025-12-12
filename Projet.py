# Master 1 Génétique | Chef du projet: Chebab Nesrine|Lien du dépôt GitHub:
https://github.com/gene-chebab/ADN-Sequence-Analysis
# Date : 08/12/2025
# - Chebab Nesrine 
# - Tahir Fatima Zahra 
# - Radjai kamilia
# - Bouaricha siham

import pandas as pd 
data = { "Séquence": [
        "ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA",
        "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT" ],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]}

df = pd.DataFrame(data)

# 2) اختيار و عرض العمود 'Longueur' 
print(df["Longueur"].
      
print("Question 3 : sélectionner les séquences dont la longueur est > 10")
seq_gt_10 = df[df["Longueur"] > 10]
print("Séquences > 10 :")
print(seq_gt_10)

print("Question 4 : calculer la moyenne du %GC avec 3 chiffres après la virgule")
moy_gc = df["Pourcentage_GC"].mean()
moy_gc = round(moy_gc, 3)
print("Moyenne GC :", moy_gc)
