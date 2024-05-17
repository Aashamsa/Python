# class myclass:                #objects = plural
#     x = 5                     #instances = singular
# p1 = myclass
# print(p1.x)

# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
# p1 =Person("John", 36)
# #print(p1.name)
# #print(p1.age)

# class name:
#     def __init__(self,name):
#         self.name = name
#     def display(self):
#         print("Hello, my name is" + self.name)

class person:
    def walk(self):
        print("Yes I can walk.")
    def run(self):
        print("Yes I can run.")
    def fly(self):
        print("No, I can't run.")
#john = person()

class myclass:
    def __init__(obj,name,age):
        obj.name = name
        obj.age = age
    def myfunc(sub):
        print("Hello my name is " + sub.name)
#p1 = myclass("John", 36)
#p1.myfunc()
#p1.age = 40
#print(p1.age)

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
class Student(Person):
    pass
#x = Person("Mike", "Olsen")
#x.printname()

# #class person:
#     def walk(self):
#         print("Yes I can walk.")
#     def run(self):
#         print("Yes I can run.")
#     def fly(self):
#         print("No, I can't fly.")
# class oldman(person):
#     def run(self):
#         print("No, I can't run.")
# man = oldman()
# man.walk()
# man.run()
# man.fly()

class person:
    def walk(self):
        print("I can walk!")
    def run(self):
        print("I can run!")
    def fly(self):
        print("NO i cant fly!")
class bird(person):
    def run(self):
        print("No i cant run....")
    def fly(self):
        print("Yes i can fly!!!!!")
bird1 = bird()
bird1.walk()
bird1.run()
bird1.fly()