# 🛒 Projeto de Preparação de Dados - Ecommerce

Este projeto tem como objetivo demonstrar a aplicação de técnicas de preparação de dados para um dataset de ecommerce. As etapas incluem tratamento de variáveis numéricas, escalonamento com MinMaxScaler e codificação de variáveis categóricas utilizando LabelEncoder, tudo com o auxílio do pandas e scikit-learn.

## 🚀 Etapas do Projeto

### 1. **Leitura e Limpeza dos Dados**
O dataset é carregado, seguido de uma análise inicial das colunas e valores únicos para entender melhor as variáveis. Colunas desnecessárias, como "Reais", "Centavos", "Condicao" e "Condicao_Atual", são descartadas.

### 2. **Escalonamento de Variáveis**
Utilizando o `MinMaxScaler` da biblioteca `scikit-learn`, são escalonadas as variáveis numéricas:
- Nota
- Número de Avaliações
- Desconto
- Preço
- Quantidade Vendida

### 3. **Codificação de Variáveis Categóricas**
Com o uso do `LabelEncoder`, são codificadas as variáveis categóricas:
- Marca
- Material
- Temporada
- Nome do Produto
- Categoria

### 4. **Verificação Final**
Uma análise dos novos valores das variáveis escalonadas e codificadas é feita, incluindo valores mínimos, máximos e médias.

## ⚙️ Tecnologias Usadas

- **Pandas**: Manipulação de dados e limpeza.
- **Scikit-learn**: Técnicas de escalonamento e codificação.
- **Python 3.x**: Linguagem utilizada para o processamento de dados.

## 📝 Como Executar

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/SEU-USUARIO/preparacao-dados-ecommerce.git
