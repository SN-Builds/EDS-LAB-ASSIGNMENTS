import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
name = input("New name: ")
age = int(input("New age: "))
new_row = {"Name": name,"Age": age}
df = df.append(new_row, ignore_index = True)
# Display the DataFrame after adding a new row
print("After adding a row:\n",df)

# Modifying a row
ind = int(input("Index of row to modify: "))
age = int(input("New age: "))

df.loc[ind, "Age"] = age



# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)

# Deleting a row
