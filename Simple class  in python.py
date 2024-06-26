class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print('Hello My Name is '+self.name)
        
class_object=Person("Abhishek",20)
class_object.myfun()
