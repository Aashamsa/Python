#list comprehension
fruits = ["apple", "banana", "mango", "cherry"]
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in range(10) if x<5]
newlist = ["Hello" for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#dictionary comprehension
keys = ["red", "yellow", "green"]
values = ["apple", "mango", "kiwi"]
mydict = {k:v for (k,v) in zip(keys,values)}
mydict = dict(zip(keys,values))
mydict = dict.fromkeys(range(5),True)
print(mydict)