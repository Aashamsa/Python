def sum(x):
    return 5 + x
print (sum(5))

def function():
    print("Hello world")
    pass

def myfunc(*,x):
    print(x)
myfunc(x = 3)

def myfunc(x,/):
    print(x)
myfunc(3)

def function(a,b,/,*,c,d):
    print(a+b+c+d)
function(1, 2, c=3, d=4)