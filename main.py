# First, what do we need? 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()

# Making sure my data is loaded and filtered to only include the columns I need.
def my_data():
    try:
        data = pd.read_csv('data/Dietary Habits Survey Data.csv')
        return data
    except FileNotFoundError:
        print("File has not been uploaded")
        return None
data = pd.read_csv('data/Dietary Habits Survey Data.csv')


# Making a function to include the choices my user will see and what will happen for each choice.
def main():
    while True:
        print("1. Analyze young adults' different food identitities.")
        print("2. Generate Visualization")
        print("3. Analyze female food identities")
        print("4. Generate Visualization 2")
        print("5. Exit Program")
        user_input = input("What would you like to do? (1-4): ")
        if user_input == "1":
            young_adult_identity()
        elif user_input == "2":
            visualization()
        elif user_input == "3":
            female_food_identities()
        elif user_input == "4":
            visualization2()
        elif user_input == "5":
            print("you are leaving")
            break

# I want my data to only count the number of adults and match that number to the corresponding food identity.
def food_identity():
    subset1 = data[['Age', 'What would best describe your diet:']]
    return subset1

def young_adult_identity():
    filtered_data = food_identity().loc[data['Age'] == '18-24']
    filtered_data = filtered_data[['What would best describe your diet:']]
    counts = filtered_data['What would best describe your diet:'].value_counts()
    print(counts)

# Generating a bar graph of my data using the filtered data I made in a previous function.
def visualization():
    filtered_data = food_identity().loc[data['Age'] == '18-24']
    filtered_data = filtered_data[['What would best describe your diet:']]
    counts = filtered_data['What would best describe your diet:'].value_counts()
    counts.plot(kind='bar')
    plt.title('Young adult food identities')
    plt.xlabel('Food identies')
    plt.ylabel('Value')
    plt.show()

# This time, I only want my data to account for women and their food indentitites.
def female_food_identity():
    subset2 = data[['Gender', 'What would best describe your diet:']]
    return subset2

def female_food_identities():
    filtered_data = female_food_identity().loc[data['Gender'] == 'Female']
    filtered_data = filtered_data[['What would best describe your diet:']]
    counts = filtered_data['What would best describe your diet:'].value_counts()
    print(counts)

# Generating a pie chart of my data using the filtered data for food identities of women.
def visualization2():
    filtered_data = female_food_identity().loc[data['Gender'] == 'Female']
    filtered_data = filtered_data[['What would best describe your diet:']]
    counts = filtered_data['What would best describe your diet:'].value_counts()
    counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Women's food identities")
    plt.show()
    
main()