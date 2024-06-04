# Ocean Environmental Prediction

## Descrição do Projeto

Este projeto utiliza técnicas de Machine Learning para prever condições ambientais marítimas, incluindo temperatura, níveis de oxigênio-18 e emissões de CO2. O objetivo é antecipar eventos prejudiciais para a vida marinha. O projeto envolve as etapas de exploração de dados, levantamento de hipótese, criação e treinamento de modelos com validações, e conclusão.

## Estrutura do Projeto

- `dataset/`: Contém todos os arquivos CSV usados no projeto.
  - `NASA GLOBAL LAND-OCEAN TEMPERATURE INDEX.csv`
  - `gso18.csv`
  - `GlobalCO2Emissions.csv`
  - `cast.csv`
  - `bottle.csv`
- `main.py`: Script principal para carregar os dados, treinar os modelos e fazer previsões.
- `historical_data_with_calcofi.png`: Gráfico dos dados históricos.
- `future_predictions_rf.png`: Gráfico das previsões futuras usando Random Forest.
- `future_predictions_knn.png`: Gráfico das previsões futuras usando KNN.

## Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas Python: pandas, matplotlib, scikit-learn

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ocean-environmental-prediction.git
   cd ocean-environmental-prediction
