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
