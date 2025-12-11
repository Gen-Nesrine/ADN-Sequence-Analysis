# tp1_solution.py
# 1) إنشاء وعرض الجدول باستعمال pandas
data = { "Séquence": [
        "ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA",
        "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT" ],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]}

df = pd.DataFrame(data)

# 2) اختيار و عرض العمود 'Longueur' 
print(df["Longueur"].
      
