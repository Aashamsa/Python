import random
num = random.randint(1,100)
count = 0
for x in range(5):
    guess = int(input("Enter a number: "))
    count += 1
    if num < guess:
        print("The number is lesser!")
    elif num > guess:
        print("The number is higher!")
    elif num == guess:
        print("----------")
        print(f"{guess} is the correct number!")
        print("----------")
if count >= 5:
    print("----------")
    print("You lost!")
    print(f"The number was {num}!")
    print("----------")