import matplotlib.pyplot as plt
import numpy as np

# Define the categories and their respective percentages for sensitivity
categories = ['Low Sensitivity', 'Medium Sensitivity', 'High Sensitivity']
sensitivity_percentages = [13.11, 50.91, 2.74]  # Percentages for low, medium, and high sensitivity

# Define player examples for each category
player_examples = {
    'Low Sensitivity': 'mwzera',  # Exemplo de jogador para sensibilidade baixa
    'Medium Sensitivity': 'aspas',  # Exemplo de jogador para sensibilidade média
    'High Sensitivity': 'wippie'  # Exemplo de jogador para sensibilidade alta
}

# Define DPI categories and their percentages
dpi_categories = ['800 DPI', '1600 DPI']
dpi_percentages = [54.46, 14.77]  # Percentages for 800 and 1600 DPI

# Create subcategory bar widths and positions
bar_width = 0.4
dpi_positions_centered = [0.5, 1.5]  # Positioning DPI bars in the center of the plot
sensitivity_positions = np.arange(len(categories))

# Define new, more vivid colors for DPI bars
dpi_colors = ['#FFD700', '#FF8C00']  # Gold and Dark orange

# Create the figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Subplot A: Sensitivity Preferences
for i, category in enumerate(categories):
    bar = ax1.bar(sensitivity_positions[i], sensitivity_percentages[i], width=bar_width, color=['blue', 'green', 'red'][i])
    # Larger and bolder percentage label inside the bar
    ax1.text(sensitivity_positions[i], sensitivity_percentages[i]/2, f'{sensitivity_percentages[i]}%',
             color='white', weight='bold', ha='center', va='center', fontsize=16)
    # Player example label above the bar
    example_player = player_examples.get(category, '')
    ax1.text(sensitivity_positions[i], sensitivity_percentages[i] + 3, example_player, color='black', weight='bold', ha='center', fontsize=12)

ax1.set_title('A) Sensitivity Preferences Among Pro Players')
ax1.set_xlabel('Sensitivity Category')
ax1.set_ylabel('Percentage of Players (%)')
ax1.set_xticks(sensitivity_positions)
ax1.set_xticklabels(categories)
ax1.set_ylim(0, 60)  # Extend y-axis to fit the labels inside and above the bars

# Subplot B: DPI Preferences
for i, dpi_setting in enumerate(dpi_categories):
    bar = ax2.bar(dpi_positions_centered[i], dpi_percentages[i], width=bar_width, color=dpi_colors[i])
    # Bold percentage label inside the bar
    ax2.text(dpi_positions_centered[i], dpi_percentages[i]/2, f'{dpi_percentages[i]}%',
             color='black', weight='bold', ha='center', va='center', fontsize=16)

ax2.set_title('B) DPI Preferences Among Pro Players')
ax2.set_xlabel('DPI Settings')
ax2.set_ylabel('Percentage of Players (%)')
ax2.set_xticks(dpi_positions_centered)
ax2.set_xticklabels(dpi_categories)
ax2.set_ylim(0, 60)  # Extend y-axis to fit the labels inside the bars

# Adjusting the font size for all text in the plots
for ax in [ax1, ax2]:
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + 
                 ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(14)

plt.tight_layout()
plt.show()
