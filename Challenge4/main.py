import matplotlib.pyplot as plt

years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

plt.plot(years,temp_anomalies, label="Temp Anomalies",marker = "o")
plt.plot(years,co2_emissions, label="Co2 Emissions",marker = "o")

plt.title("CO2 emissions and temperature anomalies over the years")
plt.legend()
plt.xlabel("Years")
# plt.ylabel("Temperature Anomalies","Co2 Emissions")
plt.grid(True)
# plt.style('Solarize_Light2')
print(plt.style.available)

plt.show()