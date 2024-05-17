a = "hello"
#print (a.lower())
#print (a.split())

def sum(a,b):
    print(a+b)
#sum(1,2)

def div(a,b):
    print (f"Division of {a} by {b} is {a/b}")
#div(8,2)

def string(a,b="Orange"):
    print(f"{a} and {b}")
#string("Apple")

#list =[1,"apple", True, 99.99]
#print(len(list))

#list= ["apple", "mango", "cherry"]
#print(type(list))

a = "apple"
#print(list(a))

#list = ["apple", "cherry", "mango"] 
#print(list[2:4])
#if "apple" in list:
    #print("Yes, apple is in the list.")
#list[1:] = ["watermelon"] 
#print(list)
#list.append( 1,"orange")
#print(list)

#list2 = ["papaya", 'kiwi', "orange"]
#list1 = ["apple", 'mango']
#list1.extend(list2)
#print(list1)

#list = ["apple", "cherry", "mango"] 
tuple = ("kiwi", "orange")
list.extend(tuple)
print(list)
list.remove ("apple")
