import pandas as pd

dados = {
    'produto': ['Livro', 'Caneta', 'Caderno'],
    'preço': [49.90, 3.50, 15.80],
    'estoque': [150, 800, 200]
}

df_produtos = pd.DataFrame(dados)

print(df_produtos)