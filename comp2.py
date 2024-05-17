newdict = {x: x*3 for x in range(10) if x*3 % 3 ==0}
newdict = {x.upper(): x*3 for x in "coding"}
print(newdict)