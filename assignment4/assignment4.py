

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

# Create a DataFrame from a dictionary:
# Use a dictionary containing the following data:
# Name: ['Alice', 'Bob', 'Charlie']
# Age: [25, 30, 35]
# City: ['New York', 'Los Angeles', 'Chicago']
# Convert the dictionary into a DataFrame using Pandas. 
# Use these exact names, ages, and cities — the tests compare your DataFrame against these exact values.
# Print the DataFrame to verify its creation.
# save the DataFrame in a variable called task1_data_frame and run the tests.

# Add a new column:
# Make a copy of the dataFrame you created named task1_with_salary (use the copy() method)
# Add a column called Salary with values [70000, 80000, 90000].
# Print the new DataFrame and run the tests.

# Modify an existing column:
# Make a copy of task1_with_salary in a variable named task1_older
# Increment the Age column by 1 for each entry.
# Print the modified DataFrame to verify the changes and run the tests.

# Save the DataFrame as a CSV file:
# Save the task1_older DataFrame to a file named employees.csv using to_csv(), do not include an index in the csv file.
# Look at the contents of the CSV file to see how it's formatted.
# Run the tests.


import pandas as pd

# Create DataFrame from a dictionary:
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# Add a new column:
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print(task1_with_salary)

# Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print(task1_older)

# Save the DataFrame as a CSV file:
task1_older.to_csv("employees.csv", index=False)


# Task 2: Loading Data from CSV and JSON

# Read data from a CSV file:
# Load the CSV file from Task 1 into a new DataFrame saved to a variable task2_employees.
# Print it and run the tests to verify the contents.

# Read data from a JSON file:
# Create a JSON file (additional_employees.json). 
# The file adds two new employees. 
# Eve, who is 28, lives in Miami, and has a salary of 60000, 
# and Frank, who is 40, lives in Seattle, and has a salary of 95000. 
# Use these exact values, with columns Name, Age, City, Salary — the tests compare the combined result exactly.
# Load this JSON file into a new DataFrame and assign it to the variable json_employees.
# Print the DataFrame to verify it loaded correctly and run the tests.

# Combine DataFrames:
# Combine the data from the JSON file into the DataFrame loaded from the CSV file 
# and save it in the variable more_employees. 
# When you combine them, reset the index so the rows are numbered 0-4 
# (for example, pass ignore_index=True to pd.concat).
# Print the combined Dataframe and run the tests.


# Read data from a CSV file:
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

# Read data from a JSON file:
json_employees = pd.read_json("additional_employees.json")
print(json_employees)

# Combine DataFrames:
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# Use the head() method:
# Assign the first three rows of the more_employees DataFrame to the variable first_three
# Print the variable and run the tests.

# Use the tail() method:
# Assign the last two rows of the more_employees DataFrame to the variable last_two
# Print the variable and run the tests.

# Get the shape of a DataFrame:
# Assign the shape of the more_employees DataFrame to the variable employee_shape
# Print the variable and run the tests.

# Use the info() method:
# Print a concise summary of the DataFrame using the info() method to understand the data types and non-null counts.


# Use the head() method:
first_three = more_employees.head(3)
print(first_three)

# Use the tail() method:
last_two = more_employees.tail(2)
print(last_two)

# Get the shape of a DataFrame:
employee_shape = more_employees.shape
print(employee_shape)

# Use the info() method:
more_employees.info()


