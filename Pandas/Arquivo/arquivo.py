import pandas as pd

df_vendas = pd.read_csv('./Arquivo/vendas.csv')

df_vendas['Total'] = df_vendas['Preco'] * df_vendas['Quantidade']

print("DataFrame com a nova coluna 'Total':")
print(df_vendas)

df_vendas.to_csv('./Arquivo/vendas_com_total.csv', index=False)
