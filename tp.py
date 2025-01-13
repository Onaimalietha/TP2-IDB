import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Carregando as tabelas
df_cadunico = pd.read_csv('cadunico.csv', sep=';', encoding='ISO-8859-1')
df_coletas = pd.read_csv('coletas.csv', sep=';', encoding='ISO-8859-1')
df_iqvu = pd.read_csv('iqvu.csv', sep=';', encoding='ISO-8859-1')
df_up = pd.read_csv('up.csv', sep=',', encoding='ISO-8859-1')

# Mesclando as tabelas com base na coluna 'regional'
print(df_cadunico.columns)
df_cadunico_up = df_cadunico.merge(df_up, on='REGIONAL', how='inner')