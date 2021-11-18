import csv
import matplotlib.pyplot as plt

# Define first function
def read_data():
    with open('titanic.csv') as file:
        csv_reader = csv.reader(file)
