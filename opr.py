num1 = int(input("Enter a number: "))
num2 = int(input('Enter a number: '))
op = input('Enter an operator "+", "-", "*", "/": ')
if op == "+":
    print("Sum = ", num1 + num2)
elif op== "-":
    print ("Difference = ", num1 - num2)
elif op == "*":
    print ("Multiplication = ", num1 * num2)
elif op == "/":
    print ("Division = ", num1 / num2)
else:
    print ("Invalid operator.")

print(f"{num1} is lesser than {num2}")