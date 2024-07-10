import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

temp_file_path = 'dataset/NASA GLOBAL LAND-OCEAN TEMPERATURE INDEX.csv'
oxygen_file_path = 'dataset/gso18.csv'
co2_file_path = 'dataset/GlobalCO2Emissions.csv'
cast_file_path = 'dataset/cast.csv'
bottle_file_path = 'dataset/bottle.csv'

print("Carregando os datasets...")
try:
    temp_data = pd.read_csv(temp_file_path)
    oxygen_data = pd.read_csv(oxygen_file_path, on_bad_lines='skip')
    co2_data = pd.read_csv(co2_file_path)
    cast_data = pd.read_csv(cast_file_path, low_memory=False)
    bottle_data = pd.read_csv(bottle_file_path, low_memory=False)
    print("Datasets carregados com sucesso!")
except FileNotFoundError as e:
    print(f"Erro ao carregar os datasets: {e}")
    exit()
except pd.errors.ParserError as e:
    print(f"Erro de parsing ao carregar os datasets: {e}")
    exit()

print("Colunas do dataset de temperatura:")
print(temp_data.columns)
print("Colunas do dataset de oxigênio-18:")
print(oxygen_data.columns)
print("Colunas do dataset de emissões de CO2:")
print(co2_data.columns)
print("Colunas do dataset CalCOFI cast:")
print(cast_data.columns)
print("Colunas do dataset CalCOFI bottle:")
print(bottle_data.columns)

required_columns = ['Cst_Cnt', 'Depthm', 'T_degC', 'O2ml_L', 'Salnty']
missing_columns = [col for col in required_columns if col not in bottle_data.columns]
if missing_columns:
    print(f"Colunas faltando no dataset bottle: {missing_columns}")
    exit()

bottle_data = bottle_data.merge(cast_data[['Cst_Cnt', 'Year', 'Month']], on='Cst_Cnt', how='left')

calcofi_data = bottle_data[['Year', 'Month', 'Depthm', 'T_degC', 'O2ml_L', 'Salnty']]
calcofi_data = calcofi_data[calcofi_data['Depthm'] <= 10]  # Considerar dados de superfície

calcofi_yearly = calcofi_data.groupby('Year').mean().reset_index()

calcofi_yearly['Year'] = calcofi_yearly['Year'].astype(int)
calcofi_yearly = calcofi_yearly.dropna(subset=['T_degC', 'O2ml_L', 'Salnty'])

oxygen_data['Year'] = pd.to_numeric(oxygen_data['Year'], errors='coerce')
oxygen_data = oxygen_data.dropna(subset=['Year'])
oxygen_data['Year'] = oxygen_data['Year'].astype(int)

co2_data['Year'] = pd.to_numeric(co2_data['Year'], errors='coerce')
co2_data = co2_data.dropna(subset=['Year'])
co2_data['Year'] = co2_data['Year'].astype(int)

temp_data['year'] = pd.to_numeric(temp_data['year'], errors='coerce')
temp_data = temp_data.dropna(subset=['year'])
temp_data['year'] = temp_data['year'].astype(int)

oxygen_data['d18O'] = pd.to_numeric(oxygen_data['d18O'], errors='coerce')
oxygen_data = oxygen_data.dropna(subset=['d18O'])

temp_col = 'Annual_mean'
oxygen_col = 'd18O'
year_col_temp = 'year'
year_col_oxygen = 'Year'
year_col_co2 = 'Year'

combined_data = temp_data.merge(oxygen_data, left_on=year_col_temp, right_on=year_col_oxygen)
combined_data = combined_data.merge(co2_data, left_on=year_col_temp, right_on=year_col_co2)
combined_data = combined_data.merge(calcofi_yearly, left_on=year_col_temp, right_on='Year')

print("Primeiras linhas do dataset combinado:")
print(combined_data.head())

correlation = combined_data[[temp_col, oxygen_col, 'Emissions', 'T_degC', 'O2ml_L', 'Salnty']].corr()
print("Correlação entre Temperatura, Níveis de d18O, Emissões de CO2 e Dados CalCOFI:")
print(correlation)

plt.figure(figsize=(12, 6))
plt.plot(combined_data[year_col_temp], combined_data[temp_col], label='Historical Temperature')
plt.plot(combined_data[year_col_temp], combined_data[oxygen_col], label='Historical d18O', linestyle='--')
plt.plot(combined_data[year_col_temp], combined_data['Emissions'], label='Historical CO2 Emissions', linestyle='-.')
plt.plot(combined_data[year_col_temp], combined_data['T_degC'], label='Sea Surface Temperature', linestyle=':')
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Historical Data: Temperature, d18O, CO2 Emissions, and Sea Surface Temperature')
plt.legend()
print("Salvando gráfico histórico...")
plt.savefig('historical_data_with_calcofi.png')
print("Gráfico histórico salvo.")

temp_threshold = 0.95
oxygen_threshold = -2.0
co2_threshold = 400


combined_data['temp_alert'] = combined_data[temp_col] > temp_threshold
combined_data['oxygen_alert'] = combined_data[oxygen_col] < oxygen_threshold
combined_data['co2_alert'] = combined_data['Emissions'] > co2_threshold

combined_data['alert'] = combined_data['temp_alert'] | combined_data['oxygen_alert'] | combined_data['co2_alert']

critical_years = combined_data[combined_data['alert']]
print("\nAnos críticos identificados nos dados históricos:")
print(critical_years)

features = combined_data[[year_col_temp, oxygen_col, 'Emissions', 'T_degC', 'O2ml_L', 'Salnty']]
target = combined_data[temp_col]

print("Dividindo os dados em treinamento e teste...")
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
print("Dados divididos com sucesso!")

print("Treinando o modelo...")
model = RandomForestRegressor(n_estimators=1000, random_state=42)
model.fit(X_train, y_train)
print("Modelo treinado com sucesso!")

future_years = pd.DataFrame({
    year_col_temp: range(2025, 2036),
    oxygen_col: [-2.1, -2.2, -2.3, -2.4, -2.5, -2.6, -2.7, -2.8, -2.9, -3.0, -3.1],
    'Emissions': [405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455],
    'T_degC': [20.1, 20.2, 20.3, 20.4, 20.5, 20.6, 20.7, 20.8, 20.9, 21.0, 21.1],
    'O2ml_L': [5.5, 5.4, 5.3, 5.2, 5.1, 5.0, 4.9, 4.8, 4.7, 4.6, 4.5],
    'Salnty': [33.5, 33.6, 33.7, 33.8, 33.9, 34.0, 34.1, 34.2, 34.3, 34.4, 34.5]
})
future_predictions = model.predict(future_years)

print("\nPrevisões de Temperatura para 2025 a 2035:")
for year, prediction in zip(future_years[year_col_temp], future_predictions):
    print(f"Ano {year}: {prediction:.2f}")

future_years['Predicted_Temperature'] = future_predictions

future_years['temp_alert'] = future_years['Predicted_Temperature'] > temp_threshold
future_years['oxygen_alert'] = future_years[oxygen_col] < oxygen_threshold
future_years['co2_alert'] = future_years['Emissions'] > co2_threshold
future_years['alert'] = future_years['temp_alert'] | future_years['oxygen_alert'] | future_years['co2_alert']

future_critical_years = future_years[future_years['alert']]
print("\nAnos críticos identificados nos dados futuros:")
print(future_critical_years)

for index, row in future_years.iterrows():
    print(f"\nAno: {row[year_col_temp]}")
    print(f"Nível de d18O: {row[oxygen_col]:.2f}")
    print(f"Emissões de CO2: {row['Emissions']}")
    print(f"Temperatura Prevista: {row['Predicted_Temperature']:.5f}")
    print(f"Alerta de Temperatura: {'Sim' if row['temp_alert'] else 'Não'}")
    print(f"Alerta de Nível de d18O: {'Sim' if row['oxygen_alert'] else 'Não'}")
    print(f"Alerta de Emissões de CO2: {'Sim' if row['co2_alert'] else 'Não'}")
    print(f"Alerta Geral: {'Sim' if row['alert'] else 'Não'}")

    if row['alert']:
        reasons = []
        if row['temp_alert']:
            reasons.append("alta temperatura")
        if row['oxygen_alert']:
            reasons.append("baixo nível de oxigênio-18")
        if row['co2_alert']:
            reasons.append("altas emissões de CO2")

        reasons_str = " e ".join(reasons)
        print(f"Alerta: Condições críticas previstas para o ano {row[year_col_temp]} devido a {reasons_str}.")

plt.figure(figsize=(12, 6))
plt.plot(future_years[year_col_temp], future_years['Predicted_Temperature'], label='Predicted Temperature', marker='o')
plt.axhline(y=temp_threshold, color='r', linestyle='--', label='Temperature Threshold')
plt.xlabel('Year')
plt.ylabel('Predicted Temperature')
plt.title('Predicted Temperature from 2025 to 2035')
plt.legend()
print("Salvando gráfico de previsões futuras...")
plt.savefig('future_predictions.png')
print("Gráfico de previsões futuras salvo.")
