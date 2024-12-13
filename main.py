# First, what do we need? 
import pandas as pd
import matplotlib.pyplot as plt

# Making sure my data is loaded and filtered to only include the columns I need.
def my_data():
    try:
        data = pd.read_csv('data/Dietary Habits Survey Data.csv')
        subset1 = data[['Age', 'What would best describe your diet:']]
        return subset1
    except FileNotFoundError:
        print("File has not been uploaded")
        return None
data = pd.read_csv('data/Dietary Habits Survey Data.csv')

# Making a function to include the choices my user will see and what will happen for each choice.
def main():
    while True:
        print("1. Analyze young adults' different food identitities.")
        print("2. Generate Visualization")
        print("3. Exit Program")
        user_input = input("What would you like to do? (1-3): ")
        if user_input == "1":
            young_adult_identity()
        elif user_input == "2":
            visualization()
        elif user_input == "3":
            print("you are leaving")
            break

# I want my data to only count the number of adults and match that number to the corresponding food identity.
def young_adult_identity():
    filtered_data = my_data().loc[data['Age'] == '18-24']
    filtered_data = filtered_data[['What would best describe your diet:']]
    counts = filtered_data['What would best describe your diet:'].value_counts()
    print(counts)

# Generating a bar graph of my data using the filtered data I made in a previous function.
def visualization():
    filtered_data = my_data().loc[data['Age'] == '18-24']
    filtered_data = filtered_data[['What would best describe your diet:']]
    counts = filtered_data['What would best describe your diet:'].value_counts()
    counts.plot(kind='bar')
    plt.title('Young adult food identities')
    plt.xlabel('Food identies')
    plt.ylabel('Value')
    plt.show()

main()