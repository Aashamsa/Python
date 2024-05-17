#prime & composite numbers
#num = int(input("Enter a number:"))
#for i in range (2,num):
#    if num % i == 0:
#       print(f"{num} is a composite number.") 
#      break
#else :
#     print (f"{num} is a prime number.")

#factors
#num = int(input("Enter a number: "))
#print (f"The factors of {num} are :")
#for i in range (1, num):
#    if num % i == 0:
#        print (i)

# Factorial
num= int(input("Enter a number: "))
factorial = 1
for i in range (1, num + 1):
    factorial =factorial*i
print(f"Factorial of {num} is {factorial}.")

#composie & prime
num = int(input("Enter a number: "))
count = 0
for i in range (1, num):
    if num % i == 0:
        count += 1
if count == 1:
    print (num,"is a prime number.")
else :
    print (num, "is a composite number.")

num1 = int(input("Enter a number:"))
operator = input ("Enter an operator:")
if (operator == "+"):
       num2 = num1 + 5
       print (num1, "+", "5", "=",num2)
       
elif (operator == "-"):
         num2 = num1 - 5
         print (num1, "-", "5", "=", num2)
         
elif (operator == "*"):
        num2 = num1 * 2
        print (num1, "*", "2", "=", num2)
        
elif (operator == "/"):
        num2 = num1 / 2
        print (num1, "/", "2", "=", num2)
       
else:
        print ("Invalid input.")    