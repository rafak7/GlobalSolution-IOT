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
