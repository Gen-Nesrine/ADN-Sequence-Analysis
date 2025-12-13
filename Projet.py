import pandas as pd

# Master 1 Génétique | Chef du projet: Chebab Nesrine
# https://github.com/gene-chebab/ADN-Sequence-Analysis
# Date : 08/12/2025
# - Chebab Nesrine
# - Tahir Fatima Zahra
# - Radjai kamilia
# - Bouaricha siham

# 1) créer et afficher le tableau
data = {
    "Séquence": [
        "ATGCGTACGTA", "GCTAGCTAGGCC", "ATGAAAGGCTT",
        "CGTACGTAGC", "TTAACCGGTT"
    ],
    "Longueur": [11, 12, 11, 10, 10],
    "Pourcentage_GC": [54.55, 66.67, 45.45, 60.0, 50.0]
}

df = pd.DataFrame(data)
print(df)

# 2) sélectionner et afficher la colonne Longueur
print(df["Longueur"])

# 3) sélectionner les séquences > 10
print("Question 3 : sélectionner les séquences > 10")
seq_gt_10 = df[df["Longueur"] > 10]
print("Séquences > 10 :")
print(seq_gt_10)

# 4) calculer la moyenne du % GC
print("Question 4 : calculer la moyenne du % GC")
moy_gc = df["Pourcentage_GC"].mean()
moy_gc = round(moy_gc, 3)
print("Moyenne GC :", moy_gc)

# 6) Ajouter une colonne comptant le nombre de 'G'
df["Nombre_G"] = df["Séquence"].str.count("G")

# 7) écart-type (sample et population)
std_sample_gc = df["Pourcentage_GC"].std(ddof=1)      # échantillon
std_population_gc = df["Pourcentage_GC"].std(ddof=0)  # population
std_sample_length = df["Longueur"].std(ddof=1)
std_population_length = df["Longueur"].std(ddof=0)

print("Écart-type (Pourcentage GC) - échantillon (ddof=1) :", round(std_sample_gc, 4))
print("Écart-type (Pourcentage GC) - population (ddof=0) :", round(std_population_gc, 4))
print("Écart-type (Longueur) - échantillon (ddof=1) :", round(std_sample_length, 4))
print("Écart-type (Longueur) - population (ddof=0) :", round(std_population_length, 4))

# sauvegarder en CSV
df.to_csv("sequence_table_final.csv", index=False)

