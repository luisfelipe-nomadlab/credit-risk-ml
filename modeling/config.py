# -*- coding: utf-8 -*-
"""config.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12dKayUOJZbIePC2J-pkQ0z4u4KXOam22
"""

# config.py

DATA_PATH = "data/credit_data.csv"
RANDOM_STATE = 42
TEST_SIZE = 0.2

NUM_FEATURES = [
    "qtd_filhos", "idade", "tempo_emprego", "qt_pessoas_residencia", "renda"
]

CAT_FEATURES = [
    "sexo", "posse_de_veiculo", "posse_de_imovel", "tipo_renda",
    "educacao", "estado_civil", "tipo_residencia"
]