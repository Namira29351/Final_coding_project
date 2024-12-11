# First, what do we need? 
import pandas as pd
import matplotlib.pyplot as plt

# Load our bus routes data
# bus_routes = pd.read_csv('data/DDOT_Bus_Routes_-_Current.csv')

# # What's in our data? Let's look!
# print("First few rows:")
# print(bus_routes.head(10))
# print(bus_routes.dtypes)

# MENU_OPTIONS = {

#     '1': 'See which busses run on Sundays',
#     '2': 'Generate Visualization',
#     '3': 'Exit program'

# }

def my_data():
    try:
        data = pd.read_csv('data/Dietary Habits Survey Data.csv')
        print("file loaded ")
        return data
    except FileNotFoundError:
        print("File has not been uploaded")
        return None
my_data()
data = pd.read_csv('data/Dietary Habits Survey Data.csv')

