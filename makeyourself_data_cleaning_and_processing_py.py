# -*- coding: utf-8 -*-
"""makeyourself-data_cleaning_and_processing.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eo9p9mD7Zju_iq1D1wHjOrgTDhuzmNuv
"""

import pandas as pd
import seaborn as srn
import statistics as sts

dataset = pd.read_csv("tempo.csv", sep=";")

dataset.head()

dataset.shape

# Variables classification
# Aparencia -> categoric
# Temperatura -> Numeric
# Umidade -> Numeric
# Vento -> Categoric
# Jogar -> Categoric

# Exploring categorical variables

# Aparencia
# Problems: The dataset has the value menos that is outside of thedomain.
aparencia_agg = dataset.groupby(["Aparencia"]).size()
aparencia_agg
aparencia_agg.plot.bar(color="gray")

# Vento
# Problemas: no have problems
vento_agg = dataset.groupby(["Vento"]).size()
vento_agg
vento_agg.plot.bar(color="gray")

# Jogar
# Problems: no have problems
jogar_agg = dataset.groupby(["Jogar"]).size()
jogar_agg
jogar_agg.plot.bar(color="gray")

# Exploring numeric variables

# Temperatura
# Problems: has outliers
dataset["Temperatura"].describe()
srn.boxplot(dataset["Temperatura"]).set_title("Temperatura")
srn.distplot(dataset["Temperatura"]).set_title("Temperatura")

# Umidade
# Problems: has outliers
dataset["Umidade"].describe()
srn.boxplot(dataset["Umidade"]).set_title("Umidade")
srn.distplot(dataset["Umidade"]).set_title("Umidade")

# Searching null values
# Umidade and Vento has null values
dataset.isnull().sum()

# Data processing

# Categoric variables
  # null values will be replaced by moda
  # values outside the domain will be replace by moda

# Numeric variables
  # null values will be replaced by median

dataset["Vento"].fillna("FALSO", inplace=True)

median = sts.median(dataset["Umidade"])
median
dataset["Umidade"].fillna(median, inplace=True)

dataset.loc[dataset["Aparencia"].isin(["menos"]), "Aparencia"] = "sol"
dataset.groupby("Aparencia").size()

dataset.loc[(dataset["Temperatura"] > 1200)]
median = sts.median(dataset["Temperatura"])
median
dataset.loc[(dataset["Temperatura"] > 1200), "Temperatura"] = median

dataset.loc[(dataset["Umidade"] >= 200)]
median = sts.median(dataset["Umidade"])
median
dataset.loc[(dataset["Umidade"] >= 200), "Umidade"] = median