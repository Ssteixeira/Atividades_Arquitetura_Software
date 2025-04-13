# -*- coding: utf-8 -*-
"""
Análise exploratória com AutoViz, Sweetviz e D-Tale
Utilizando kagglehub para carregar o dataset diretamente do Kaggle
"""

# Importação das bibliotecas
import os
import pandas as pd
import matplotlib.pyplot as plt
import dtale
from autoviz.AutoViz_Class import AutoViz_Class
import sweetviz as sv
import kagglehub

# Baixar o dataset diretamente do Kaggle
print("📥 Baixando dataset do Kaggle...")
path = kagglehub.dataset_download("sebastianwillmann/beverage-sales")
print("✅ Dataset baixado em:", path)

# Caminho completo para o arquivo CSV dentro da pasta baixada
file_path = os.path.join(path, "synthetic_beverage_sales_data.csv")

# Carregar o DataFrame
try:
    df = pd.read_csv(file_path)
    print("✅ Dataset carregado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar o CSV: {e}")
    exit()

# Exibir informações básicas
print("\n📄 Informações do DataFrame:")
df.info()
print("\n🔍 Primeiras 10 linhas:")
print(df.head(10))
print("\n📊 Estatísticas descritivas:")
print(df.describe().round())
print("\n📊 Estatísticas para colunas categóricas:")
print(df.describe(include=["object", "category"]))
print("\n🚨 Valores ausentes:")
print(df.isnull().sum())

# Visualização com AutoViz
print("\n🔎 Gerando relatório com AutoViz...")
av = AutoViz_Class()
report = av.AutoViz(file_path)

# Visualização com Sweetviz
print("\n✨ Gerando relatório com Sweetviz...")
sweet_report = sv.analyze(df)
sweet_report.show_html("sweetviz_report.html")
print("✅ Relatório Sweetviz salvo como 'sweetviz_report.html'")

# Visualização interativa com D-Tale
print("\n🚀 Abrindo D-Tale...")
d = dtale.show(df)
d.open_browser()
