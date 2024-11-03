# Creating a set
my_set = {1, 2, 3, 4, 4}  # Duplicate 4 is automatically removed
print(my_set) 

# Adding an element
my_set.add(5)
print(my_set)  

# Removing an element
my_set.discard(3)
print(my_set) 

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)  
print(set_a & set_b)  
print(set_a - set_b) 
