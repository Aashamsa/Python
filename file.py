names = open("file.txt", "wt")
for x in range(0,6):
    name = input("Enter a name: ")
    if "a" in name:
        names.write(f"{name} \n")
names.close()

f = open("file.txt", "rt")
print(f.read())
f.close()