#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#print([num for num in a if num < 5])
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# prints all elements in a which are less than 5
print("prints all elements in a which are less than 5")
for i in a:
    if i < 5:
        print(i)

# Above code in one line
print("Above code in one line")
print([i for i in a if i < 5])

# creates a new list a_new with all the numbers less than 5 from list a
print("creates a new list a_new with all the numbers less than 5 from list a")
a_new = []
for i in a:
    if i < 5:
        a_new.append(i)
        print(a_new)

# Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than that number given by the user.
print("Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.")
num = int(input("Please enter a number: "))
for i in a:
    if i < num:
        print(i)
'''
Take a list, say for example this one:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''