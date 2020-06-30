usernum = int(input("Enter a number: "))
divisible = int(2)
print(usernum)
if usernum % divisible == 0:
    print(f"Even number: {usernum / divisible}")
else:
    print(f"Odd number: {usernum / divisible}")
if usernum % 4 == 0:
    print("Multiple of four")
else:
    print("Not a multiple of four")
num = int(input("Enter a number: "))
check = int(input("Enter another number: "))
if check % num == 0:
    print(check % num)
else:
    print("Not evenly divisible!")