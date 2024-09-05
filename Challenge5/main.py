import csv
import matplotlib.pyplot as plt

def generate_population_dictionary_from_csv(filename):
  
  """Generating population from csv data"""
  with open(filename, 'r') as csvfile:
    population_per_continent = {}

    
    reader = csv.DictReader(csvfile)
    for line in reader:
      continent = line['continent']
      year = int(line['year'])
      population = int(line['population'])

      if continent not in population_per_continent:
        population_per_continent[continent] = {'population': [], 'years': []}
        
      population_per_continent[continent]['population'].append(population)
      population_per_continent[continent]['years'].append(year)
      
  return population_per_continent
"""Returns a dictionary following the structure"""

filename = 'Challenge5/data.csv'
population_per_continent = generate_population_dictionary_from_csv(filename)
  
  
def generate_plot_from_dictionary(population_dictionary):
  """Function to generate plot from population dictionary"""
  
  for continent in population_dictionary:
    years = population_dictionary[continent]['years']
    population = population_dictionary[continent]['population']
    plt.plot(years, population, label=continent, marker="o", alpha=0.5)
    
  plt.title("Internet Population per continent")
  plt.xlabel("Year")
  plt.ylabel("Internet users (in billion users)")
  plt.grid(True)
  plt.tight_layout()
  plt.legend()
  
  plt.show()
    
    
generate_plot_from_dictionary(population_per_continent)
  



