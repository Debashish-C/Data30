num = int(input("Enter a number: "))

print("Multiplication Table using for loop:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


num = int(input("Enter a number: "))

print("Multiplication Table using while loop:")
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
