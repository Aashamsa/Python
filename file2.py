f = open("myfile.txt", "wt")
num = int(input("Enter a number of entries: "))
for x in range(0,num):
    names = input("Enter a name: ")
    if "a" in names:
        f.write(f"{names} \n")
f.close()
f = open("myfile.txt", "rt")
print(f.read())
f.close