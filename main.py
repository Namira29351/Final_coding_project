# First, what do we need? 
import pandas as pd
import matplotlib.pyplot as plt

# MENU_OPTIONS = {

#     '0': 'Analyze which meal people think is most important',
#     '1': 'Analyze young adults different food identitities',
#     '2': 'Generate Visualization',
#     '3': 'Exit program'

# }

def my_data():
    try:
        data = pd.read_csv('data/Dietary Habits Survey Data.csv')
        # print("file loaded ")
        # num_column = len(data.columns)
        # print(num_column)
        subset1 = data[['Age', 'What would best describe your diet:']]
        # num_column = len(subset1.columns)
        # print(num_column)
        return subset1
    except FileNotFoundError:
        print("File has not been uploaded")
        return None
# my_data()
data = pd.read_csv('data/Dietary Habits Survey Data.csv')

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

def young_adult_identity():
    filtered_data = my_data().loc[data['Age'] == '18-24']
    filtered_data = filtered_data[['What would best describe your diet:']]
    
    counts = filtered_data['What would best describe your diet:'].value_counts()
    print(counts)


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