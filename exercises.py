import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# ===================== EXERCÍCIO 1 =====================
# Carrega o dataset original
df = pd.read_csv('/data/ecommerce_tratados.csv')
pd.set_option('display.width', None)

# Verifica dados únicos
unicos = df.nunique()
print('===== Análise de dados únicos =====\n', unicos)

# Estatísticas descritivas
estatisticas = df.describe()
print('\n===== Estatísticas dos dados =====\n', estatisticas)

# Cria campo Preço
df['Preco'] = df['Reais'] + (df['Centavos'] / 100)

# Remove colunas desnecessárias
df.drop(columns=['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'], inplace=True)


# ===================== EXERCÍCIO 2 =====================
# Mantém apenas colunas úteis
df = df[['Nota', 'N_Avaliacoes', 'Desconto', 'Preco', 'Marca', 'Material', 'Temporada', 'Qtd_Vendidos', 'Nome', 'Categoria']]

# Escalonamento com MinMaxScaler
scaler = MinMaxScaler()
df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])
df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliacoes']])
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])

# Codificação com LabelEncoder
label_encoder = LabelEncoder()
df['Marca_Cod'] = label_encoder.fit_transform(df['Marca'])
df['Material_Cod'] = label_encoder.fit_transform(df['Material'])
df['Temporada_Cod'] = label_encoder.fit_transform(df['Temporada'])


# ===================== EXERCÍCIO 3 =====================
# MinMaxScaler para Qtd_Vendidos
df['Qtd_Vendidos_Cod'] = scaler.fit_transform(df[['Qtd_Vendidos']])

# LabelEncoder para Nome e Categoria
df['Nome_Cod'] = label_encoder.fit_transform(df['Nome'])
df['Categoria_Cod'] = label_encoder.fit_transform(df['Categoria'])

# ===================== VERIFICAÇÕES FINAIS =====================
print('\n===== Resumo das novas variáveis (MinMax) =====')
for col in ['Nota_MinMax', 'N_Avaliacoes_MinMax', 'Desconto_MinMax', 'Preco_MinMax', 'Qtd_Vendidos_Cod']:
    print(f"{col} - Min: {df[col].min():.4f}, Max: {df[col].max():.4f}, Mean: {df[col].mean():.4f}, Std: {df[col].std():.4f}")
    print('---------------------------------------------')

print('\n===== Códigos LabelEncoder =====')
for col in ['Marca_Cod', 'Material_Cod', 'Temporada_Cod', 'Nome_Cod', 'Categoria_Cod']:
    print(f"{col} - Valores únicos: {df[col].nunique()}")
print('===================================')
