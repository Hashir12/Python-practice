# List is mutable
exampleList = [1,2,3,4,5,6]

# length of the list
print(len(exampleList))

# getting the index of any item from the start of the list
print(exampleList[0])

# getting the index of any item from the end of the list
print(exampleList[-1]) # => 6
print(exampleList[-2]) # => 5

# Slicing the list
print(exampleList[0:3]) # => [1,2,3]
print(exampleList[-3:]) # => [4,5,6]
print(exampleList[-3:-1]) # => [4,5]