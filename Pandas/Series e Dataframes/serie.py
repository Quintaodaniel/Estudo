import pandas as pd

# Dados
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador']
populacoes = [12396372, 6775561, 2530701, 2900319]

serie = pd.Series(data=populacoes, index=cidades)

print(serie)