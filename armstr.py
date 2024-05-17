num = int(input("Enter a number: "))
length = len(str(num))
digit = 0
sum = 0
temp = num
for i in range(length):
    digit = temp % 10
    temp = temp // 10
    sum += digit**length
if sum == num:
    print(num, "is an armstrong number.")
else:
    print(num, "is not an armstrong number.")