import pandas as pd

# Carica i dati (assicurati che i file siano in formato CSV)
df_mini = pd.read_csv('mini.csv', header=None)
df_nano = pd.read_csv('nano.csv', header=None)

# Rimuovi il trattino e converte in numerico (se necessario)
df_mini[0] = df_mini[0].str.rstrip('-').astype(int)
df_nano[0] = df_nano[0].str.rstrip('-').astype(int)

# Trova gli elementi unici in ciascun DataFrame
unique_mini = set(df_mini[0])
unique_nano = set(df_nano[0])

# Trova gli elementi in NANO ma non in MINI
only_in_nano = unique_nano - unique_mini
print("Elementi solo in NANO:", only_in_nano)

# Trova gli elementi in MINI ma non in NANO
only_in_mini = unique_mini - unique_nano
print("Elementi solo in MINI:", only_in_mini)
