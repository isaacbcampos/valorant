import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Dados dos ranks e suas respectivas porcentagens
data = {
    'Rank': [
        'Iron 1', 'Iron 2', 'Iron 3', 
        'Bronze 1', 'Bronze 2', 'Bronze 3', 
        'Silver 1', 'Silver 2', 'Silver 3', 
        'Gold 1', 'Gold 2', 'Gold 3', 
        'Platinum 1', 'Platinum 2', 'Platinum 3', 
        'Diamond 1', 'Diamond 2', 'Diamond 3', 
        'Ascendant 1', 'Ascendant 2', 'Ascendant 3', 
        'Immortal 1', 'Immortal 2', 'Immortal 3', 'Radiant'
    ],
    'Percentage': [
        0.871, 2.612, 6.332, 
        6.1, 9.09, 8.004, 
        9.603, 8.626, 8.537, 
        7.763, 6.192, 5.005, 
        4.565, 3.7, 3.308, 
        2.084, 2.427, 1.681, 
        1.132, 0.635, 0.329, 
        0.183, 0.081, 0.032, 0.028
    ]
}

# Cores para cada rank
colors = [
    '#a3a3a3', '#808080', '#505050', # Iron
    '#cd7f32', '#c0c0c0', '#ffd700', # Bronze
    '#c0c0c0', '#a8a8a8', '#8f8f8f', # Silver
    '#ffd700', '#ffc000', '#ffab00', # Gold
    '#b9f2ff', '#89e4ff', '#55d6ff', # Platinum
    '#f0e68c', '#e6dc32', '#dbd300', # Diamond
    '#ff4f00', '#ff4500', '#ff3a00', # Ascendant
    '#ff0000', '#e60000', '#cc0000', # Immortal
    '#ffd700' # Radiant
]

# Criando DataFrame
df = pd.DataFrame(data)

# Definindo o estilo do gráfico
plt.style.use('seaborn-whitegrid')
sns.set_context("talk")

# Criando o gráfico de barras
plt.figure(figsize=(10, 8))
barplot = sns.barplot(x='Percentage', y='Rank', data=df, palette=colors)

# Adicionando os valores em cada barra
for index, value in enumerate(df['Percentage']):
    barplot.text(value, index, f'{value:.2f}%', color='black', ha="left", va="center")

# Ajustando os títulos e labels
plt.xlabel('Percentage (%)', fontsize=12)
plt.ylabel('Rank', fontsize=12)
plt.title('Valorant Rank Distribution - Brazilian Server', fontsize=14)

# Mostrando o gráfico
plt.tight_layout()
plt.show()
