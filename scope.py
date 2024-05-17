x = 23
def myfunc():
    global x
    x = 21
myfunc()
print(x)