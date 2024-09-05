import csv
import matplotlib.pyplot as plt

filename = 'Challenge2/data.csv'

with open(filename, 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    continent = line['continent']
    year = line['year']
    population = line['population']

    print(continent)
    print(year)
    print(population)
    print(line)
    
plt.plot([2000, 2010, 2020, 2030], [100, 200, 300, 400], label="Europe", marker="o")
plt.plot([2000, 2010, 2020, 2030], [200, 300, 500, 800], label="Asia", marker="o")

plt.title("Internet Population per continent")
plt.xlabel("Year")
plt.ylabel("Internet users")
plt.grid(True)
plt.legend()

plt.show()
  