# class student:
#     """Student data"""
# print(id(student))
# obj1=student
# obj2=student
# obj3=student
# print(id(obj1),id(obj2),id(obj3))

# class student:
#     """student data"""
#     def __init__(self):
#         print(id(self))
#         print("external constructor called")
# obj=student()
# print(id(student),id(obj))

# class student:
#     """data of student"""      
#     def __init__(self):
#         print("user made constructor")
#         print(id(self))
# obj1=student()
# print(id(student),id(obj1))
# print(student.__doc__)
# print(dir())
# print(__name__)
# class student:
#     school='shss'
#     def __init__(self,name):
#         self.n=name
#         student.principal='python'

#     def add_new(self, contact):
#         self.c=contact
#         student.city='city'
#         x=10
# student.school_code=101
# obj=student('neeraj')
# obj.email='ygmail.com'
# class student:
#     school='shss'
#     def __init__(self,name):
#         self.n=name
#         student.principal='python'
#         print(student.school_code)
#     def add_new(self,contact):
#         self.c=contact
#         student.city='bhopal'
#         print(student.school_code,student.principal,student.city)
#         x=10
# student.school_code=101
# obj=student('yash')
# obj.email='yemail.com'
# obj.add_new(1234)
# print(student.city)
# class mobile:
#     def __init__(self,name,brand):
#         self.name=name
#         self.brand=brand
#     def check(self):
#         print(f'this is a {self.name} {self.brand}')
# obj1=mobile("samsung","y91")
# obj2=mobile("vivo",'y100')
# obj1.check()
# obj2.check()
# class student:
#     school="abc school"  
#     @classmethod
#     def change_school(cls,new_school):
#         cls.school=new_school
# student.change_school('xyz school')
# print(student.school)
# obj=student()
# obj.change_school("mno school")
# print(student.school)

# --------------------------------------------------
# class student:
#     school="abc school"

#     @classmethod
#     def change_school(cls,new_school):
#         student.school=new_school

# obj=student()
# obj.change_school('xyz school')
# print(student.school)
# print(student.school)
# student.change_school('mno')
# print(student.school)
# -------------------------------------------------

# class student:
#     school="xyz school"

#     @classmethod
#     def school_change(cls,new_school):
#         student.school=new_school

# print(student.school)
# obj=student()
# print(student.school)
# student.school_change('abc school')
# print(student.school)
# -------------------------------------------------

# class student:
#     school='shss'
#     def __init__(self,name):
#         self.n=name
#         student.principal='python'
#         print(student.school_code)
#     def add_new(self,contact):
#         self.c=contact
#         student.city='bhopal'
#         print(student.school_code,student.principal,student.city)       
#         x=10
# student.school_code=101
# obj=student('yash')
# print(student.school_code,student.principal)
# obj.email='y@gmail.com'
# obj.add_new(1234)
# ---------------------------------------------

# class student:
#     school='shss'
#     def __init__(self,name):
#         self.n=name
#         print(self.n)
   
#     def add_new(self,contact):
#         self.c=contact
#         print(self.n,self.c,self.school_code,self.x)
#         x=10
#         print(self.x)
    
# obj=student('yash')
# obj.x=20
# obj.school_code=101
# obj.add_new(12344)
# print(obj.school_code,obj.n,obj.c)

# class animal:
#     def speak(self):
#         print("animal speaks")
# class dog(animal):
#     def bark(self):
#         print("dog barks")
# obj=dog()
# obj.speak()
# obj.bark()

# class animal:
#     def speaks(self):
#         print("animal speaks")
# class dog(animal):
#     def bark(self):
#         print("dog barks")
# obj=dog()
# obj.speaks()
# obj.bark()

# class grand:
#     def home(self):
#         print("grandparents gave home")
# class father(grand):
#     def car(self):
#         print("father gave car")
# class child(father):
#     pass
# obj=child()
# obj.home()
# obj.car()
# class A:
#     def mess(self):
#         print("this is from A class")
# class B(A):
#     def message(self):
#         print("B class")
# obj=B()
# obj.message()
# obj.mess()

# Abstraction -------------------------------------

# from abc import ABC,abstractmethod

# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
    
#     @abstractmethod
#     def stop(self):
#         pass
# class car(vehicle):
#     def start(self):
#         print("car start")
#     def stop(self):
#         print("car stop")
# obj=car()
# obj.start()
# obj.stop()
        
# class student:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def show(self):
#         print(f"my name is {self.n} and i am {self.a} years old ")
# obj=student("yash",21)
# obj.show()

# class student:
#     def __init__(self,name,age):
#         self.__name=name
#         self._age=age
#         self.rollno=101
#     def show(self):
#         print(self.__name,self._age,self.rollno)
# obj=student('yash',21)
# obj.show()
# print(obj.rollno)
# print(obj._age)
# print(obj.__name)



