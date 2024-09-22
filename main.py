import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filename):
    """Carrega os dados do CSV."""
    dados = pd.read_csv(filename)
    return dados

def analyze_data(dados):
    """Realiza a análise dos dados e retorna um dicionário com os resultados."""
    tipos_variaveis = dados.dtypes
    escalas_variaveis = {col: 'numérica' if pd.api.types.is_numeric_dtype(dados[col]) else 'categórica' for col in dados.columns}
    valores_faltantes = dados.isnull().sum()
    medidas_descritivas_numericas = dados.describe()
    medidas_descritivas_categoricas = dados.describe(include='object')
    filhos_frequentes = dados['filhos'].mode()[0]
    percentual_fumantes = dados['fumante'].value_counts(normalize=True) * 100
    contagem_regiao = dados['regiao'].value_counts()

    # Exibindo resultados
    print("Tipos e Escalas:\n", tipos_variaveis)
    print("\nEscalas:\n", escalas_variaveis)
    print("\nValores Faltantes:\n", valores_faltantes)
    print("\nMedidas Descritivas Numéricas:\n", medidas_descritivas_numericas)
    print("\nMedidas Descritivas Categóricas:\n", medidas_descritivas_categoricas)
    print("\nNúmero de Filhos mais Frequente:", filhos_frequentes)
    print("\nPercentual de Clientes Fumantes:\n", percentual_fumantes)
    print("\nContagem de Categorias na Região:\n", contagem_regiao)

    return {
        "Tipos e Escalas": tipos_variaveis,
        "Escalas": escalas_variaveis,
        "Valores Faltantes": valores_faltantes,
        "Medidas Descritivas Numéricas": medidas_descritivas_numericas,
        "Medidas Descritivas Categóricas": medidas_descritivas_categoricas,
        "Número de Filhos mais Frequente": filhos_frequentes,
        "Percentual de Clientes Fumantes": percentual_fumantes,
        "Contagem de Categorias na Região": contagem_regiao
    }

def plot_data(dados):
    """Gera gráficos para visualizar os dados."""
    plt.figure(figsize=(12, 5))

    # Gráfico de Distribuição da Idade
    plt.subplot(1, 2, 1)
    sns.histplot(dados['idade'], bins=20, kde=True, color='blue')
    plt.title('Distribuição da Idade')
    plt.xlabel('Idade')
    plt.ylabel('Frequência')

    # Gráfico de Contagem de Clientes Fumantes
    plt.subplot(1, 2, 2)
    sns.countplot(x='fumante', data=dados, palette='Set2', hue='fumante')
    plt.title('Clientes Fumantes')
    plt.xlabel('Fumante')
    plt.ylabel('Contagem')

    plt.tight_layout()
    plt.show()

def main():
    dados = load_data('seguro_de_vida.csv')
    results = analyze_data(dados)
    plot_data(dados)

if __name__ == "__main__":
    main()
