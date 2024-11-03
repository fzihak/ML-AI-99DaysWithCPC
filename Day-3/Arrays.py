from array import array

# Creating an array of integers
numbers = array('i', [1, 2, 3, 4, 5])
print(numbers) 

# Accessing elements
print(numbers[2])  

# Appending an element
numbers.append(6)
print(numbers)
