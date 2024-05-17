thisset= {"apple", "banana", "cherry", "apple"}
print(thisset)
for x in thisset:
    print(x)
print("banana" in thisset)
tropical =("pineapple", "mango", "papaya")
thisset.update(tropical)
print(thisset)
thisset.discard("kiwi")
print(thisset)
x = thisset.pop()
print (x)
print(thisset)
