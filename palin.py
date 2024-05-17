num = int(input("Enter a number: "))
d = num
temp = 0
res = 0
while num != 0 :
    hold = num % 10
    res = (res*10) + hold
    num = int(num / 10)
if d == res:
    print(res, "is a palindrome.")
else:
    print(res, "is not a palindrome.")