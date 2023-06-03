# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with Pickling Data and Exception Handling
# Dev : Amruth D
# ChangeLog (Who,When,What):
# Amruth D,02ndJune2023,created script to complete assignment 07
# ---------------------------------------------------------------------------- #

# This code demonstrates the usage of pickle module to save and load data from a file and Structured error handling

import pickle

# Data
strFileName = 'AppData.dat'  # File name for storing data
lstCustomer = []  # List to store customer data

# Processing
def save_data_to_file(file_name, list_of_data):
    # Save the data to a binary file using pickle
    with open(file_name, 'wb') as file:
        pickle.dump(list_of_data, file)
    print(f"Data saved to {file_name}")

def read_data_from_file(file_name):
    # Read the data from a binary file using pickle
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
    return data

# Presentation
while True:
    try:
        # Get ID and NAME from the user and store it in a list object
        customer_id = input("Enter customer ID (or 'q' to quit): ")
        if customer_id == 'q':
            break

        # Check if the customer ID is a valid integer
        if not customer_id.isdigit():
            raise ValueError("Invalid customer ID. Please enter an integer value.")

        customer_name = input("Enter customer name: ")

        # Check if the customer name is a non-integer value
        if customer_name.isdigit():
            raise ValueError("Invalid customer name. Please enter a non-integer value.")

        # Create a dictionary to store customer details and add it to the list
        customer = {'id': int(customer_id), 'name': customer_name}
        lstCustomer.append(customer)
    except ValueError as e:
        # Handle ValueError exceptions and print error messages
        print(e)

# Store the list object into a binary file
save_data_to_file(strFileName, lstCustomer)

# Read the data from the file into a new list object and display the contents
loaded_data = read_data_from_file(strFileName)

print("Loaded Data:")
for customer in loaded_data:
    # Print the customer ID and name for each customer in the loaded data
    print(f"ID: {customer['id']}, Name: {customer['name']}")
    print()
    print()

# Wait for the user to press Enter before exiting
print(input("Press Enter to Exit the program: "))

