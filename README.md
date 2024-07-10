# 🌊 GlobalSolution-IOT

## 📜 Descrição do Projeto

Este projeto utiliza técnicas de Machine Learning para prever condições ambientais marítimas, incluindo temperatura, níveis de oxigênio-18 e emissões de CO2. O objetivo é antecipar eventos prejudiciais para a vida marinha. O projeto envolve as etapas de exploração de dados, levantamento de hipótese, criação e treinamento de modelos com validações, e conclusão.

## 📂 Estrutura do Projeto

- `dataset/`: Contém todos os arquivos CSV usados no projeto.
  - `🌡️ NASA GLOBAL LAND-OCEAN TEMPERATURE INDEX.csv`
  - `🌍 gso18.csv`
  - `🏭 GlobalCO2Emissions.csv`
  - `🔍 cast.csv`
  - `🧪 bottle.csv`
- `main.py`: Script principal para carregar os dados, treinar os modelos e fazer previsões.
- `📈 historical_data_with_calcofi.png`: Gráfico dos dados históricos.
- `📊 future_predictions_rf.png`: Gráfico das previsões futuras usando Random Forest.

## 🛠️ Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas Python: pandas, matplotlib, scikit-learn

## 💻 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/GlobalSolution-IOT.git
   cd GlobalSolution-IOT
   
2. Crie um ambiente virtual e instale as dependências:
bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

## 🧑‍🏫 Uso

1. Coloque os arquivos CSV no diretório dataset/.
2. Execute o script principal:
`python main.py`

3. Verifique os gráficos gerados:
📈 historical_data_with_calcofi.png: Visualiza os dados históricos.
📊 future_predictions_rf.png: Visualiza as previsões futuras usando Random Forest.

## 📑 Estrutura do Código
Carregamento dos Dados
Os dados são carregados a partir de arquivos CSV. Os datasets incluem:

• Dados de temperatura global da NASA.
• Níveis de oxigênio-18.
• Emissões de CO2.
• Dados do programa CalCOFI.

## Preparação dos Dados
Os dados são combinados em um único DataFrame com base no ano. Colunas são convertidas para o tipo correto e valores faltantes são tratados.

Treinamento dos Modelos
Um modelo de Machine Learning é usado:

• Random Forest

## Previsão para Anos Futuros
Previsões são feitas para os próximos 10 anos (2025-2035). Alertas são gerados se os valores previstos ultrapassarem determinados limiares críticos.

## Visualização
Gráficos são gerados para visualizar os dados históricos e as previsões futuras.

## 📊 Resultados Esperados
Os resultados esperados incluem previsões precisas das condições ambientais marítimas para os próximos 10 anos. Alertas são gerados para anos críticos onde as condições podem ser prejudiciais para a vida marinha.

## 🔍 Metodologia
• Exploração de Dados: Análise inicial dos dados para entender suas características.
• Levantamento de Hipótese: Proposição de hipóteses sobre a relação entre diferentes variáveis.
• Treinamento de Modelos: Utilização de Random Forest para treinar modelos preditivos.
• Validação e Avaliação: Validação dos modelos usando dados de teste e métricas de desempenho.
• Previsão e Geração de Alertas: Previsão das condições futuras e geração de alertas críticos.

## 🔗 Link Download do projeto: 
https://mega.nz/file/VilCQDKK#dc1STisOnkA3WuxxFLCSv4FJkchezfpGpSuMNIaShQA

## 🧪 Exemplos de Uso
Aqui estão alguns exemplos de como usar o script principal para gerar previsões e alertas:

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Python-blue.svg" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Ocean%20Conservation-Big%20Data-green.svg" alt="Ocean Conservation">
</p>
🛠️ Ferramentas Utilizadas
IDE: Pycharm
<p align="center">
  <img src="https://resources.jetbrains.com/storage/products/pycharm/img/meta/pycharm_logo_300x300.png" alt="Pycharm" width="100">
</p>
Linguagem: Python
<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python" width="150">
</p>
Bibliotecas: pandas, matplotlib, scikit-learn
<p align="center">
  <img src="https://pandas.pydata.org/static/img/pandas_mark.svg" alt="pandas" width="100">
  <img src="https://media.licdn.com/dms/image/D4D12AQFq38cGkv_oHQ/article-cover_image-shrink_423_752/0/1679493396295?e=1723075200&v=beta&t=e-cA-ge5gzIDJRcEFZgQoqIYuBUjkHJ6RhRyqXSLSHE" alt="matplotlib" width="100">
  <img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" alt="scikit-learn" width="100">
</p>
