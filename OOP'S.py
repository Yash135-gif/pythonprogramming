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
class student:
    school='shss'
    def __init__(self,name):
        self.n=name
        student.principal='python'
        print(student.school_code)
    def add_new(self,contact):
        self.c=contact
        student.city='bhopal'
        print(student.school_code,student.principal,student.city)
        x=10
student.school_code=101
obj=student('yash')
obj.email='yemail.com'
obj.add_new(1234)
print(student.city)





