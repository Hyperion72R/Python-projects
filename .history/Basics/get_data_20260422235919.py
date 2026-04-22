import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

# ---------------------------

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)

hottest_day = df.loc[df['max_temp'].idxmax()]


# -----------------------------------------------------------------


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Annotate each data point with max and min temperature values on the plot,
# then find indices of the overall highest and lowest temperatures

for i in range(len(df)):
    plt.text(df['date'][i], df['max_temp'][i] + 0.5,
             f"{df['max_temp'][i]:.0f}", ha='center')
    plt.text(df['date'][i], df['min_temp'][i] - 1,
             f"{df['min_temp'][i]:.0f}", ha='center')

max_idx = df['max_temp'].idxmax()
min_idx = df['min_temp'].idxmin()


# Annotate the highest temperature point

plt.annotate(
    'Highest',
    (df['date'][max_idx], df['max_temp'][max_idx]),
    textcoords="offset points",
    xytext=(0, 10),
    ha='center'
)

# Annotate the lowest temperature point

plt.annotate(
    'Lowest',
    (df['date'][min_idx], df['min_temp'][min_idx]),
    textcoords="offset points",
    xytext=(0, -15),
    ha='center'
)

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()


# -----------------------------------------------------------------


def plot_column(df, column_name):

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame")

    df[column_name].plot()
    plt.title(f"Plot of {column_name}")
    plt.xlabel("Index")
    plt.ylabel(column_name)
    plt.show()

    data = pd.DataFrame({
        'values': [1, 3, 2, 5, 4]
    })


plot_column(data, 'values')
