 # Your Name: Antony Abraham
 # Date: 17 JUNE 2026
 # Assignment Name: P2LAB2
 # A brief description of the project: Assignment tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user

# Instructions:
# For this assignment, you will write a program that creates a dictionary where the key and value pairs are as follows:
# Camaro : 18.21, Prius : 52.36, Model S : 110, Silverado : 26
#The keys represent an automobile, and the value represents the MPG for that vehicle.
#After creating the dictionary, create a variable that holds all the keys in the dictionary using the code below.
# keys = list(my_dict.keys())

# Print the variable that holds the keys.
# Next, prompt the user to enter one of the vehicles from the dictionary. Keep in mind the key must look exactly the same as it does in the dictionary. Python is case-sensitive.
# Display the mpg for the vehicle that the user entered.
# Prompt the user to enter the number of miles that they will drive the vehicle
# Calculate the gallons of gas needed to drive the specified vehicle the given number of miles.
# Display the gallons of gas needed, rounded to two decimal places. Use an f-string. 
# Test your car with multiple different inputs for the vehicle AND how many miles you will drive. 



# Create the dictionary that holds all the keys in the dictionary using the code below. 
car_Dict = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}


# Print the variable that holds the keys.

print("car_dict" + str(car_Dict))

# Prompt the user to enter one of the vehicles from the dictionary. Keep in mind the key must look exactly the same as it does in the dictionary. Python is case-sensitive.

vehicle = input("\nEnter a vehicle to see its mpg: ")
if vehicle in car_Dict:
    print(f"\nThe {vehicle} gets {car_Dict[vehicle]} mpg.")

    # Prompt the user to enter the number of miles that they will drive the vehicle

    miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

    # Calculate the gallons of gas needed to drive the specified vehicle the given number of miles.

    gallons = miles / car_Dict[vehicle]

    # Display the gallons of gas needed, rounded to two decimal places.  

    print(f"\n{gallons:.2f} gallons of gas are needed to drive the {vehicle} {miles} miles.")

else:
    print("\nVehicle not found among available vehicles.")



