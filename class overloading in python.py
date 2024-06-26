class Area:
    def find_area(self,var1=None,var2=None):  #overloading 
        if var1!=None and var2!=None:
            print('area is',var1*var2)
        elif var1!=None:
            print('area ',var1*var1)
        else:
            print('Nothing to print')
obj=Area()
obj.find_area() #withoght parameter

obj.find_area(10) #when passing parameter for var1

obj.find_area(10,2) #when passing parameter var1 and var2 both


#Overrriding
class Abhi:
    def display(self):
        print('Abhishek')
class Abhi2(Abhi):
    def display(self):
        print('Gautam')
obj=Abhi2()
obj.display()
