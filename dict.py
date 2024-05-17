thisdict = {
    "brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}
print(thisdict["brand"])
print(len(thisdict))
x = thisdict.get("brand")
print(x)
x = thisdict.keys()
print(x)
thisdict["colour"] = ["white"]
print(x)