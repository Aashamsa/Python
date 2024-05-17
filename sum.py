num = int(input("Enter a number: "))
sum = 0
temp = 0
while num != 0:
    hold = num % 10
    sum = sum + hold
    num = int(num/10)
print (sum)