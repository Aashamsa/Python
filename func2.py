def my_function(*kids):
    for x in kids:
        print("The name is " + x)
#my_function("Emil","Tobias", "Linus")

def my_func(lname,fname):
    print(fname + " " + lname)
#my_func(fname = "Emil", lname = "Abcde")

def a_func(**kid):
    print("His last name is " + kid["lname"])
#a_func(fname = "Tobias", lname = "Rafsnas")

def fruit_func (food):
    for x in food :
        print(x)
fruits = ["apple", "cherry"]
#fruit_func(fruits)