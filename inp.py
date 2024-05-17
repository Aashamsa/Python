num= int(input("Enter a number: "))
if num % 2 == 0:
    if num < 20 :
        print(f"{num} is an even number.")
        num = num*20
        print("Multiplication = ", num)
    elif num > 20 :
        num = num/10
        print("Division = ", num)
else :
    print ("Error. Given input is an odd number.")