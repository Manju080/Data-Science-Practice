'''from io import BufferedRandom
from unicodedata import name
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno= rollno
        self.lap = self.Laptop()  #initializing the object of inner class in outer class

    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'hp'
            self.ram=8
            self.gen = 'i5'

s1= Student('Aishu',2)
s2=Student('manju',1)   

'''
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).______(th2ickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))
    

    
    
