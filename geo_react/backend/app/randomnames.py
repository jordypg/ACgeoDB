import csv
import random

def read_names_from_csv(filename):
    with open(filename, 'r') as file:
        names = []
        for line in file:
            names.extend([name.strip() for name in line.strip().split(',')])
    return names

def generate_random_name():
    food_names = read_names_from_csv('app/food_names.csv')
    fish_names = read_names_from_csv('app/fish_names.csv')

    first_name = random.choice(food_names)
    last_name = random.choice(fish_names)
    return f"{first_name} {last_name}"
