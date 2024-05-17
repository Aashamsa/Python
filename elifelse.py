a = int(input("Enter the 1st number: "))
b= int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))
if a>b and a>c:
    print (f"{a} is greater than both {b} and {c}.")
elif b>c and b>a:
    print (f"{b} is greater than both {a} and {c}.")
elif c>a and c>b:
    print (f"{c} is greater than both {a} and {b}.")
elif a==b==c:
    print("They are equal to eachother.")