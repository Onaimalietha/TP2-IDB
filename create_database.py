import sqlite3
import pandas as pd

# List of CSV files and their corresponding table names
csv_files = [
    ('cadunico.csv', 'cadunico'),
    ('coletas.csv', 'coletas'),
    ('iqvu.csv', 'iqvu')
]


# Create SQLite database and insert data
conn = sqlite3.connect('TP2_database.db')

# Loop through each CSV file, load it into a DataFrame, and insert into the database
for csv_file, table_name in csv_files:
    df = pd.read_csv(csv_file, delimiter=';', encoding='ISO-8859-1')
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()

# repeat for fockin up because different delimiter
csv_file = 'up.csv'
df = pd.read_csv(csv_file, delimiter=',', encoding='ISO-8859-1')
df.to_sql('up', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
