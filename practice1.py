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
# n=int(input("enter: "))
# for i in range(1,n+1):
#     is_prime=False
#     for j in range(2,int(i*0.5)+1):
#         if i%j==0:
#             is_prime=True
#             break
#     if i==1:
#         print(i,end=" ")
#     if is_prime:
#         print(i,end=" ")

# string='yash'
# list_s=string.split()
# print(list_s)
# list_ss=list_s.reverse()
# print(list_ss)
# print(list_ss)

# s='yash'
# ss=''
# for i in s:
#     ss=i+ss
# print(ss)

# class A:
#     def __init__(self):
#         print("A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("C")
# obj=C()

# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         super().show()
#         print("B")
# class C(B):  
#     def show(self):
#         super().show()
#         print("C")

# obj=C()
# obj.show()

l=[3,3,5,2,4,8,3,3]
# min=l[0]
# for i in l:
#     if min>i:
#        min=i
# print(min)
# min=l[0]
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         min=l[i]
#         l[i],l[i+1]=l[i+1],l[i]
#     else:
#         min=l[i+1]
# print(min)
# max=l[0]
# for i in l:
#     if max<i:
#         max=i
# print(max)
# max=l[0]
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         max=l[i]
#         l[i],l[i+1]=l[i+1],l[i]
#     else:
#         max=l[i+1]
# print(max)

