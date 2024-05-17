mydict = {
    "child1":{
        "name": "Ram",
        "age":12
    },
    "child2":{
        "name":"Hari",
        "age":14
    },
    "child3":{
        "name":"Sita",
        "age":10
    }
}
#print(mydict["child3"]['name'])
for x,obj in mydict.items():   #prints the key i.e child1,2,etc
    print(x)                   
    for y in obj:              #prints the keys and values of the child i.e name,age,etc
        print(y + ":", obj[y])