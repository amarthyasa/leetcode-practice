# Define a dictionary with fruit names as keys and numbers as values
fruits = {'watermelon': 1, 'apple': 2, 'banana': 3}

# Sorting the dictionary based on the values (ascending order)
# sorted(fruits.items(), key=lambda item: item[1]) sorts the items in the dictionary
# based on the value (item[1] refers to the value in the key-value pair)
a = sorted(fruits.items(), key=lambda item: item[1])
print(a)
sorted_by_value = {fruit: number for fruit, number in sorted(fruits.items(), key=lambda item: item[1])}

# Sorting the dictionary based on the values (descending order)
# The only difference is we set reverse=True to sort in descending order
sorted_by_value_reverse = {fruit: number for fruit, number in sorted(fruits.items(), key=lambda item: item[1], reverse=True)}

# Display the sorted dictionaries
print("Dictionary sorted by values (ascending):", sorted_by_value)
print("Dictionary sorted by values (descending):", sorted_by_value_reverse)
