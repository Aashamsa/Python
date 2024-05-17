x = input()
try:
    print(x)
except NameError:
    print("Variable is not give.")
except:
    print("Something went wrong.")