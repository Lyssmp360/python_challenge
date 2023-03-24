import os
import csv


csvpath = os.path.join('..', 'Resources', 'budget_data')

with open("budget_data.csv",encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")