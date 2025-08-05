import matplotlib.pyplot as plt
import pandas as pd
import random as rd
from datetime import timedelta,datetime
start_date = datetime(2024, 5, 1)
date = [start_date + timedelta(days=i) for i in range(30)]
temperature=[round(rd.uniform(25, 40),1) for _ in range(30)]
rainfall=[rd.randint(40, 90) for _ in range(30)] 
humidity=[round(rd.uniform(0, 20), 1) for _ in range(30)]
for i in range(30):
    print(f"Date: {date[i].strftime('%Y-%m-%d')}")
    print(f"  Temperature: {temperature[i]} °C")
    print(f"  Humidity   : {humidity[i]} %")
    print(f"  Rainfall   : {rainfall[i]} mm")
    print("-" * 30)
Data={
    'Date': [d.strftime('%Y-%m-%d') for d in date],
    'Temperature': temperature,
    'Humidity': humidity,
    'Rainfall': rainfall
}
df=pd.DataFrame(Data)
print(df)
plt.plot(df['Date'], df['Temperature'], color='black', marker='.', linewidth=1, label='Temperature')
plt.title("Daily Temperature (May 2024)", fontsize=8)
plt.xlabel("Date", fontsize=8)
plt.ylabel("Temperature (°C)", fontsize=8)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(df['Date'], df['Rainfall'], color='skyblue', label='Rainfall')
plt.title("Daily Rainfall (May 2024)", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Rainfall (mm)", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


plt.figure(figsize=(6, 5))
plt.scatter(df['Temperature'], df['Humidity'], color='green', label='Humidity vs Temperature')
plt.title("Humidity vs Temperature", fontsize=14)
plt.xlabel("Temperature (°C)", fontsize=12)
plt.ylabel("Humidity (%)", fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
