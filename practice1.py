# n=int(input("enter rows: "))
# i=1
# while i<=n:
#     print(" "*(n-i),end="")
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     j=i-1
#     while j>=1:
#         print(j,end="")
#         j=j-1
#     print()
#     i=i+1

# def add_five(n):
#     return n+5

# def add_once(func,x):
#     return func(x)

# print(add_once(add_five,4))

# def reversing(sentence):
#     str=""
#     l1=[]
#     for char in sentence:
#         if char==" ":
#             if str:
#                 l1.append(str)
#                 str=""
#         else:
#             str=str+char

#     if str:
#         l1.append(str)

#     reverse_string=""
#     for i in range(len(l1)-1,-1,-1):
#         reverse_string=reverse_string+l1[i]
#         if i!=0:
#             reverse_string=reverse_string+" "
#     return reverse_string
# user_input=input("enter a string to reverse print: ")
# print(reversing(user_input))

# from collections import Counter
# s="aabbccaa"
# dict=Counter(s)
# print(f"counter is {dict}")
# l=["yash1","yash2","yash3"]
# s=" ".join(l)
# print(s)
# l=["name","age","quali"]
# # d2=dict.fromkeys(l)
# # print(d2)
# print(d1.get("name"))
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d1.setdefault("city","bhopal")
# d1.setdefault("name","yash1")
# print(d1)
# d1={"name":"yash","age":21,"quali":"BCA"}
# d1.update(name="yash1",city="bhopal")
# print(d1)
# s={10,230,29,38}
# print(s)
# print(type(s))
# class student:
#   def __init__(self):
#     print("constructor called")
#     print(id(self))
# obj=student()
# obj.__init__()
# print(id(obj),id(student))
# class student:
#     school="SHSS"
#     def detail(self,name,email,contact):
#         print(name,email,contact)
#         print(id(self))
# obj1=student()
# print(obj1.school)
# print(obj1.detail("yash","hfsafh",4953))
# obj2=student()
# print(obj2.school)
# print(obj2.detail("yoo","doubleyoo",34943))
# print(id(obj1),id(obj2),id(student))
# class student:
#     def __init__(self):
#         print(id(self))
# obj=student()
# print(id(student))
# print(id(obj))
# class student:
#     def __init__(self,name,grad):
#         self.n=name
#         self.g=grad
# obj=student("yash","BCA")
# print(obj.n)
# print(obj.g)
# def new():
#     global x
#     x=10
#     return x
# print(new())
# print(x)
# s={1,2,3,"yash"}
# s.clear()
# print(s)
# s={1,2,3,"yash"}
# s.add(4)
# print(s)
# s.update([5,6])
# print(s)
# s={1,12,3}
# s1=s.copy()
# print(s1)
# s={1,2,3}
# s.pop()
# print(s)
# s.pop()
# print(s)
# s={1,2,3,4,4}
# s.remove(4)
# print(s)
# s.discard(4)
# print(s)
# print(s.union(s1))
# print(s.intersection(s1))
# print(s.intersection_update(s1))
# print(s)
# print(s.difference(s1))
# print(s1.difference(s))
# print(s.difference_update(s1))
# print(s)
# print(s.symmetric_difference(s1))
# print(s1.symmetric_difference(s))
# s.symmetric_difference_update(s1)
# print(s)
# s1.symmetric_difference_update(s)
# print(s1)
# s={1,2,3,4,5,6}
# s1={5,6,7,8}
# a=frozenset(s)
# b=frozenset(s1)
# print(type(a),type(b))
# print(a.isdisjoint(b))
# print(a.isdisjoint(b))


