# Reversing a string ----------------------

# n=input("enter a string: ")
# rev=n[::-1]
# print(rev)

# Reversing a string ---------------------

# n=input("enter a string: ")
# rev=""
# for i in n:
#     rev=i+rev
# print(rev)

# Checking if a string is a palindrome string --------------------

# string=input("enter a string to check for palindorme: ")
# rev=""
# for i in string:
#     rev=i+rev
# if string==rev:
#     print("the given string is palindrome")
# else:
#     print("given string is not a palindrome string")

#   Checking is a string is anagram or not -------------------------

# string1=input("enter string 1: ")
# string2=input("enter string 2: ")
# if len(string1)!=len(string2):
#     print("not a anagram string")
# else:
#     is_anagram=True
#     for i in string1:
#         if string1.count(i)!=string2.count(i):
#             is_anagram=False
#             break
#     if not is_anagram:
#         print("not an anagram")
#     else:
#         print("angaram")
    
# Counting vowels and consonent in a string ---------------------------

# string=input("enter a string to count vowels or string: ")
# vowels="aeiouAEIOU"
# count_vowels=0
# count_consonent=0
# for i in string:
#     if i.isalpha():
#         if i in vowels:
#             count_vowels=count_vowels+1
#         else:
#             count_consonent=count_consonent+1
# print("vowels is",count_vowels)
# print("consonent is",count_consonent)

# Find the first non-repeating character in a string ---------------------

# s = "aabbcddex"
# count={}
# for char in s:
#     if char in count:
#         count[char]=count[char]+1
#     else:
#         count[char]=1
# for char in s:
#     if count[char]==1:
#         print(f"the first non-repeating character is {char}")
#         break
# else:
#   print(f"not a single non-repeating character in a given string")

# Remove duplicates from a string ------------------------------

# s="aabbccdeaf"
# result=""
# seen=set()
# for i in s:
#     if i not in seen:
#         result=result+i
#         seen.add(i)
# print(result)

# Small calculator using match case --------------------------------

# num1=int(input("enter no. 1: "))
# num2=int(input("enter no. 2: "))
# print(" + for addition \n - for substraction \n * for multiplication \n \ for division: ")
# operator=input("enter which operation you want to perform: ")
# match operator:
#     case "+":
#         print(num1+num2)
#     case "-":
#         print(num1-num2)
#     case "*":
#         print(num1*num2)
#     case "/":
#         print(num1/num2)
#     case _:
#         print("enter a valid operator")

# Good Question ------------------------------------

# input_string=input("enter string 1: ")
# n=int(input("Enter n: "))

# alphabets="abcdefghijklmnopqrstuvwxyz"
# reverse_alphabets=alphabets[::-1]
# dict1=dict(zip(alphabets,reverse_alphabets))

# prefix=input_string[0:n-1]
# suffix=input_string[n-1: ]

# mirror=""
# for i in range(len(suffix)):
#     mirror=mirror+dict1[suffix[i]]

# res=prefix+mirror
# print("the result is",res)

# Checking if string is a valid identifier -------------------------------

# import keyword

# string=input("koi string dalo: ")

# if string.isidentifier() and not keyword.iskeyword(string):
#     print(f"{string} is a valid identifier")
# else:
#     print(f"{string} not a valid indentifier")

# Checking if a valid identifier with function ------------------------

# import keyword

# def is_valid_identifier(s):
#     if not s.isidentifier():
#         return False
#     if keyword.iskeyword(s):
#         return False
#     return True

# test_strings=["yash","1yash","boy","_boy"]
# for i in test_strings:
#     print(f"{i} is valid identifier? {is_valid_identifier(i)}")

# Checking if string is a valid pythod identifier with logic -----------------------------

# import keyword

# s = input("Koi string daalo: ")

# # Check 1: Empty string
# if not s:
#     print("Invalid: Empty string ❌")
# # Check 2: First character
# elif not (s[0].isalpha() or s[0] == '_'):
#     print("Invalid: First character letter ya underscore nahi hai ❌")
# # Check 3: Rest of the characters
# elif not all(c.isalnum() or c == '_' for c in s):
#     print("Invalid: Sirf letters, digits, ya underscore hone chahiye ❌")
# # Check 4: Keyword check
# elif s in keyword.kwlist:
#     print("Invalid: Python keyword hai ❌")
# else:
#     print("Valid Python identifier ✅")

# Checking for if a number is prime or not ----------------------------------

# n = int(input("enter a number to check for prime number: "))
# is_prime=True
# for i in range(2,int(n*0.5)+ 1):
#     if n%i==0:
#         is_prime=False
#         break
# if is_prime:
#     print("the given number is a prime number")
# else:
#     print("not a prime number")
    
# swapping two variables without using third variable ----------------------

# num1=int(input("enter a number 1: "))
# num2=int(input("enter a number 2: "))

# print(num1,num2)

# num1=num1+num2
# num2=num1-num2
# num1=num1-num2

# print(num1,num2)

# finding even squares of list using map and filter  -----------------------------

# l=[1,2,3,4,5]
# def squares(num):
#     return num**2
# square_result=list(map(squares,l))
# def even(num):
#     if num%2==0:
#         return num
# even_square=list(filter(even,square_result))
# print(even_square)

# Q1: Reverse words in a sentence without using in-built split() or reversed() -------------------------------------

# def reverse_words(sentence):
#     words=[]
#     word=""
#     for char in sentence:
#         if char==" ":
#             if word:
#                 words.append(word)
#                 word=""
#         else:
#             word=word+char

#     if word:
#         words.append(word)
    
#     reversed_sentence=""
#     for i in range(len(words)-1,-1,-1):
#         reversed_sentence=reversed_sentence+words[i]
#         if i!=0:
#             reversed_sentence=reversed_sentence+" "
        
#     return reversed_sentence
# user_input=input("enter the string: ")
# print(reverse_words(user_input))

# Q2: Check if two strings are anagrams or not    (Note: Ignore case and spaces)

# def is_anagram(sentence1,sentence2):
#     sentence1=sentence1.replace(" ","").lower()
#     sentence2=sentence2.replace(" ","").lower()
#     if len(sentence1)!=len(sentence2):
#         print("not an anagram")
#     else:
#         is_anagram=False
#         for i in sentence1:
#             if sentence1.count(i)!=sentence2.count(i):
#                 is_anagram=True
#                 break
#         if not is_anagram:
#             print("both string is anagram")
#         else:
#             print("not")
# user_input1=input("enter a string1: ")
# user_input2=input("enter a string2: ")
# is_anagram(user_input1,user_input2)

# Q3: Find the second largest number in a list without using max() or sort() ---------------------------------

# l=[10,5,20,8,25]
# first=0
# second=0
# for i in l:
#     if i>first:
#         second=first
#         first=i
#     elif i>second and i!=first:
#         second=i
# print(f"first = {first}")
# print(f"second = {second}")

# Q4: Count frequency of each character in a string ----------------------------

# s="aabbccaa"
# dict1={}
# for char in s:
#         dict1[char]=dict1.get(char,0)+1
# print("the frequency is ",dict1)
            
# Use map() to convert all names to uppercase. ----------------------

# l=['yash', "yash1", 'yash3']
# def up(word):
#     x=word.upper()
#     return x
# result=list(map(up,l))
# print(result)

# Use filter() to select names starting with "A". ---------------------------
# 
# l=['avengers','a','yash']
# def select(word):
#     word=word.lower()
#     if word[0]=="a":
#         return word
# result=list(filter(select,l))
# print(result)    

# Use reduce() to concatenate all names into a single string. ---------------------------

# from functools import reduce
# l=['yash','python','cpp']
# result=reduce(lambda x,y: x+" "+y,l)
# print(result)

# Use filter() to get numbers divisible by 2. -------------------------

# l=[2,5,8,11,15]
# def divisible_by_2(num):
#     if num%2==0:
#         return num
# result=list(filter(divisible_by_2,l))
# print(result)

# Use filter() to get numbers divisible by 2. -------------------------

# l=[2,5,8,11,15]
# divisible_by_2=list(filter(lambda x: x if x%2==0 else None,l))
# print(divisible_by_2)

# Use map() to subtract 1 from each number. ----------------

# l=[2,5,8,11,15]
# result=list(map(lambda x: x-1,l))
# print(result)

# Use reduce() to multiply all numbers together. -------------------------

# from functools import reduce

# l=[1,2,3,4,5]
# result=reduce(lambda x,y: x*y,l)
# print(result)

# Given a list of numbers, use map() and lambda to convert them to their cubes. ---------------------------

# nums = [1, 2, 3, 4, 5]
# cube=list(map(lambda x: x**3,nums))
# print(cube)

# Use filter() and lambda to find all numbers divisible by 3 and greater than 10. ------------------------

# nums = [3, 6, 12, 15, 20, 21, 8]
# result=list(filter(lambda x: x if x%3==0 and x>10 else None,nums))
# print(result)

# Use reduce() and lambda to find the maximum number from a list. ----------------------

# from functools import reduce

# nums = [4, 9, 1, 22, 17]
# result=reduce(lambda x,y: x if x>y else y,nums)
# print(result)

# Given a list of names, use map() to convert all names to uppercase, and then use filter() to select those which start with "S".

# names = ["salman", "Ali", "sara", "Ahsan", "Saba"]
# result_uppercase=list(map(lambda word: word.upper(),names))
# result_S=list(filter(lambda word: word if word[0]=='S'else None,result_uppercase))
# print(result_S)

# 🔹 Q5. List of numbers: [5, 10, 15, 20, 25]
# Use map() to double all numbers
# Then use filter() to select numbers greater than 30
# Then use reduce() to calculate their sum  ------------------------------------

# from functools import reduce

# l=[5, 10, 15, 20, 25]
# double_numbers=list(map(lambda x: x+x,l))
# tees_sa_badi=list(filter(lambda x: x if x>30 else None,double_numbers))
# sum=reduce(lambda x,y: x+y,tees_sa_badi)
# print(sum)

# 🔹 Q6. Given a list of strings, use reduce() to join them with a hyphen - between each word. -----------------------

# from functools import reduce

# words = ["hello", "world", "python", "rocks"]
# answer=reduce(lambda x,y: x+"-"+y,words)
# print(answer)

# Use map() with a lambda to extract the length of each word in a sentence. -----------------------------------

# sentence="python is awesome and fun"
# list_of_string=sentence.split()
# result=list(map(lambda word: len(word),list_of_string))
# print(result)

# create your own higher order function that takes a function and a list app the function using map() and returns the list --------------------

# l=[1,2,3,4]
# def square(num):
#     return num*num
# def apply_cal(func,i):
#     return [func(i) for i in l]
# print(apply_cal(square,l))

# Checking if the number is prime or not ------------------------

# num=int(input("enter a number: "))
# is_prime=True
# for i in range(2,int(num*0.5)+1):
#     if num%i==0:
#         is_prime=False
#         break
# if is_prime:
#     print("given number is a prime number")
# else:
#     print("given number is not a prime number")

# finding the prime number till given n ----------------------------------

# num=int(input("enter till which number you want prime numbers: "))
# for i in range(2,num+1):
#     is_prime=True
#     for j in range(2,int(i*0.5)+1):
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(i,end=" ")

# Fibonacci series ----------------------

# num=int(input("enter how much fibonacci numbers you want: "))
# a,b=0,1
# for _ in range(num):
#     print(a,end=" ")
#     a,b=b,a+b

# Removing duplicates form list -----------------------

# l=[1,2,3,3,2,3,5,5,]
# seen=set()
# new_list=[]
# for num in l:
#     if num not in seen:
#         seen.add(num)
#         new_list.append(num)
# print(new_list)

#  Checking if a number is armstrong ---------------------------

# n=int(input("enter a number to check for armstrong: "))
# x=n
# y=str(n)
# length=len(y)
# sum=0
# while n>0:
#     sum=sum+(n%10)**length
#     n=n//10
# if x==sum:
#     print(f"given number {x} is armstrong")
# else:
#     print(f"given number {x} is not armstrong")

# checking for armstrong ------------------------

# n=int(input("enter a number to check for armstrong: "))
# x=y=n
# digit=0
# sum=0
# while x>0:
#     digit=digit+1
#     x=x//10
# while y>0:
#     sum=sum+(y%10)**digit
#     y=y//10
# if sum==n:
#     print(f"given number {sum} is armstrong")
# else:
#     print(f"given number {n} is not armstrong")

# Harshad number check -----------------------------------

# num=int(input("enter a number to check for harshad number: "))
# x=num
# sum=0
# while x>0:
#     a=x%10
#     sum=sum+a
#     x=x//10
# if num%sum==0:
#     print("harshad number")
# else:
#     print("not")
    
# Perfect number check ------------------------------

# num=int(input("enter to check for perfect number: "))
# sum=0
# for i in range(1,int(num*0.5)+1):
#     if num%i==0:
#         sum=sum+i
# if num==sum:
#     print("perfect number")
# else:
#     print("not")

# Strong number check -----------------------------

# num=int(input("enter to check for strong number: "))
# x=num
# sum=0
# while x>0:
#     facto=1
#     for i in range(1,(x%10)+1):
#         facto=facto*i
#     x=x//10
#     sum=sum+facto
# if sum==num:
#     print("Strong number")
# else:
#     print("not")

# Automorphic number check ------------------------------

# num=int(input("enter a number to check for automorphic number: "))
# square=num**2
# if str(square).endswith(str(num)):
#     print("the number is automorphic number")
# else:
#     print("not")

# Spy number check ---------------------------

# num=int(input("enter to check for spy number: "))
# x=num
# sum=0
# multi=1
# while x>0:
#     sum=sum+x%10
#     multi=multi*x%10
#     x=x//10
# if sum==multi:
#     print("spy number")
# else:
#     print("not")

# Neon number check -------------------------------

# num=int(input("enter to check for neon number: "))
# square=num**2
# sum=0
# while square>0:
#     sum=sum+square%10
#     square=square//10
# if num==sum:
#     print("neon number")
# else:
#     print("not")

# Pattern question -----------------------

# n=int(input("enter a number: "))
# for i in range(1,n+1):
#     print("*"*i)

# Pattern question ----------------------

# n=int(input("enter rows: "))
# for i in range(n,0,-1):
#     print("*"*i)

# pattern question ---------------------------

# n=int(input("enter rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))

# pattern question -------------------------

# n=int(input("enter rows: "))
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))

# pattern question --------------------

# n=int(input("enter rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)

# pattern question -------------------------

# n=int(input("enter rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# pattern question ---------------------

# n=int(input("enter rows: "))
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(i,end="")
#     print()

# pattern question ----------------------------

# n=int(input("enter rows: "))
# count=1
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#       print(count,end="")
#       count=count+1
#     print()

# pattern question -------------------

# n=int(input("enter rows: "))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()

# decorator question -------------------

# def even_to_odd(func):
#     def inner(n):
#         result=func(n)
#         result=list(map(lambda x: x-1,result))
#         return result
#     return inner
# def even_numbers(n):
#     l=[]
#     for i in range(1,n+1):
#         if i%2==0:
#             l.append(i)
#     return l
# x=even_to_odd(even_numbers)
# n=int(input("enter: "))
# res=x(n)
# print(res)

# decorator question --------------------------

# def even_to_odd(func):
#     def inner(n):
#         result=func(n)
#         result=list(map(lambda x: x-1,result))
#         return result
#     return inner
# @even_to_odd
# def even_numbers(n):
#     l=[]
#     for i in range(1,n+1):
#         if i%2==0:
#             l.append(i)
#     return l
# n=int(input("enter: "))
# print(even_numbers(n))

# ---------------------------------------------

# single Inheritance -------------------

# class A:
#     def message1(self):
#         print("A message")
# class B(A):
#     def message2(self):
#         print("B message")
# obj=B()
# obj.message1()
# obj.message2()

# Multilevel Inheritance -----------------------

# class A:
#     def showA(self):
#         print("This is A")
# class B(A):
#     def showB(self):
#         print("This is B")
# class C(B):
#     def showC(self):
#         print("This is C")
# obj=C()
# obj.showA()
# obj.showB()
# obj.showC()

# Multiple Inheritance ------------------------------

# class father:
#     def showfather(self):
#         print("rep father")
# class mother:
#     def showmother(self):
#         print("rep mother")
# class child(father,mother):
#     def showchild(self):
#         print("rep child")
# obj=child()
# obj.showfather()
# obj.showmother()

# Heirarichal Inheritance ------------------

# class parent:
#     def show(self):
#         print('this is parent')
# class child1(parent):
#     def showchild1(self):
#         print("this is child1")
# class child2(parent):
#     def showchild2(self):
#         print("this is child2")
# obj=child1()
# obj1=child2()
# obj.show()
# obj1.show()

# Multiple Inheritance --------------------

# class A:
#     def show(self):
#         print("A")
# class B:
#     def show(self):
#         print("B")
# class C(B,A):
#     pass
# obj=C()
# obj.show()

# herierical Inheritance ----------------

# class A:
#     def showA(self):
#         print("A")
# class B(A):
#     def showB(self):
#         print("B")
# class C(A):
#     def showC(self):
#         print("C")
# obj=C()
# obj.showC()
# obj.showA()

# obj1=B()
# obj1.showB()
# obj1.showA()

# overriding -------------------------

# class animal:
#     def speaks(self):
#         print("animal speaks")
# class dog(animal):
#     def speaks(self):
#         super().speaks()
#         print("dog barks")
# obj=dog()
# obj.speaks()

# hybrid Inheritance ---------------------------------

# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
# class C(A):
#     def show(self):
#         print("C")
# class D(C,B):
#     def show(self):
#         super().show()
#         print("D")
# obj=D()
# obj.show()

# hybrid -----------------------------

# class A:
#     def showA(self):
#         print("A")
# class B(A):
#     def showB(self):
#         print("B")
# class C(A):
#     def showC(self):
#         print("C")
# class D(B,C):
#     def showD(self):
#         print("D")
# obj=D()
# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()

# factor nikalna ka tarika --------------------

# n=int(input("enter a number: "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")

# ascending order ma rakhna ka liya ---------------------

# l=[1,2,3,4,3,2,3,2,5]
# n=len(l)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# Arranging in descinding order --------------------

# l=[1,2,4,2,3,3,2,2,3,2]
# n=len(l)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if l[j]<l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# finding maximum digit in a list ---------------------------

# l=[1,2,3,4,3,2,3]
# sum=l[0]
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         sum=l[i]
#         l[i],l[i+1]=l[i+1],l[i]
#     else:
#         sum=[i+1]
# print(f'maximum digit {sum}')

# finding minimun digit in a list ----------------------------

# l=[2,3,2,1,4,5,6,3,4]
# min=l[0]
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         min=l[i]
#         l[i],l[i+1]=l[i+1],l[i]
#     else:
#         min=l[i+1]
# print(f"minumum digit: {min}")    

# Abstraction --------------------------------

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

# polymorphism ---------------------

# class player:
#     def show(self):
#         print("players runs")

# class enemy:
#     def show(self):
#         print("enemy crawls")

# class NPC:
#     def show(self):
#         print("Walks")

# character=[player(),enemy(),NPC()]
# for i in character:
#     i.show()

#  Example of polymorphism ---------------

# class creditcard:
#     def pay(self,amount):
#         print(f"pay through creditcard amount {amount}")
# class paypal:
#     def pay(self,amount):
#         print(f"pay through paypal amount {amount}")
# class UPI:
#     def pay(self,amount):
#         print(f"pay through UPI amount {amount}")

# def process_payment(payment_method,amount):
#     payment_method.pay(amount)

# payments=[creditcard(),paypal(),UPI()]

# for method in payments:
#     process_payment(method,500)

# Example -------------------------

# class book:
#     def __init__(self,pages):
#         self.pages=pages
    
#     def __add__(self,other):
#         print(f"self.pages = {self.pages}")
#         print(f"other.pages = {other.pages}")
#         return self.pages+other.pages

# b1=book(100)
# b2=book(200)
# b3=b1+b2
# print(b3)

# overloading in python --------------

# class Calculator:
#     def add(self, *args):
#         return sum(args)

# calc = Calculator()
# print(calc.add(5))             
# print(calc.add(5, 10))         
# print(calc.add(5, 10, 15, 20))

# overriding in python ----------------------

# internet sa dhund lo

# operator overloading (+) ki ----------------------------------

# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return point(self.x+other.x,self.y+other.y)
#     def display(self):
#         print(self.x,self.y,sep=',')
# obj1=point(2,4)
# obj2=point(3,6)
# obj3=obj1+obj2
# obj3.display()

# decorator question ------------------

# def mydecorator(func):
#     def wrapper(name):
#         print('before function called')
#         func(name)
#         print('after function called')
#     return wrapper

# @mydecorator
# def greet(name):
#     print('hello ' + name)

# greet('yash')

# generator question ---------------------

# def count_up_to(n):
#     i=1
#     while i<=n:
#         yield i
#         i=i+1

# for num in count_up_to(5):
#     print(num)

# generator question ----------------

# def increament():
#     for i in range(10):
#         yield i

# for num in increament():
#     print(num)
    
# generator question ------------

# def increament(n):
#     for i in range(n):
#         yield i

# inc=increament(10)
# print(next(inc))
# print(next(inc))
# print(next(inc))




