import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-arya/main/temperature_data.json"
df = pd.read_json(url)

# drop row 3 -> day = wednesday
df = df[df['day'] != 'Wednesday'].reset_index(drop=True)

# fill average value -> humidity -> nan
df['humidity_pct'] = df['humidity_pct'].fillna(df['humidity_pct'].mean())

# new cols -> farenheit  | cell*1.8 -> + 32
df['temperature_f'] = df['temperature_c'] * 1.8 + 32

# subplots -> pie,
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Pie chart - condition counts
df['condition'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=axes[0])
axes[0].set_title('Weather Condition Distribution')
axes[0].set_ylabel('')

# Bar chart - temperature by day
axes[1].bar(df['day'], df['temperature_c'], color='orange')
axes[1].set_title('Temperature by Day (°C)')
axes[1].set_xlabel('Day')
axes[1].set_ylabel('Temperature (°C)')
plt.xticks(rotation=45)

plt.tight_layout()

# save image data
plt.savefig('weather_chart.png')
df.to_csv('weather_data.csv', index=False)

plt.show()

print(df)