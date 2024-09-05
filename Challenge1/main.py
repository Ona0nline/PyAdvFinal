import csv

with open("Challenge1/data.csv","r") as file:
  csv_reader = csv.DictReader(file)
  
  for line in csv_reader:
    print(f"In {line['year']} there were {line['population']} people in {line['continent']}")
    # print(f"In {line[1]}, there were {line[2]} people in {line[0]}. ")