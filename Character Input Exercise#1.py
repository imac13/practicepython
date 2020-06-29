user = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"The users' name is {user}, and they are {age} years old")
year2020 = 2020

while age < 100:
    print("You are not 100 years yet!")
    age += 1
    currentage = age
    year2020 += 1
    print(f"Your current age is {currentage}.")
    year100 = year2020
    if age >= 100:
        print(f"You are 100 years old in the year {year100}")

