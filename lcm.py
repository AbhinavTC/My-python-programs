# defining a function to calculate LCM  
# def calculate_lcm(x, y):
#     # selecting the greater number
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while (True):
#         if ((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
#
#
# # taking input from users
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# # printing the result for the users
#
# print("The L.C.M. of", num1, "and", num2, "is", calculate_lcm(num1, num2))

# factorial using recursion

# def recursion_fact(n):
#     if n == 1:
#        return n
#     else:
#         return n*recursion_fact(n-1)
# num = int(input("Enter a number:"))
# if num<0:
#     print("Sorry the factorial does not exist")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     print("The factorial of", num, "is",recursion_fact(num))

# lambda function

# x = lambda a:  a+10
# print(x(5))

# x = lambda a,b : a*b
# print(x(5,6))

# x= lambda  a,b,c:a+b+c
# print(x(4,7,9))

# def myfun(n):
#     return lambda a: a*n
# mydoubler = myfun(2)
# print(mydoubler(11))


# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = person("John",36)
# print(p1.name)
# print(p1.age)

# import datetime
# x= datetime.datetime.now()
# print(x)

# import datetime
# x= datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))
#
# def calculate_hcf(x,y):
#     if x>y:
#        smaller=y
#     else:
#        smaller=x
#     for i in range(1,smaller+1):
#         if ((x % i==0))and(y%i==0):
#          hcf =i
#     return hcf
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# print("The HCF of",num1,"and",num2,"is",calculate_hcf(num1,num2))

# import re
# def isvalid(s):
#     pattern = re.compile("(0|91)?[7-9][0-9]{9}")
#     return pattern.match(s)
# s=input()
# if(isvalid(s)):
#     print("valid number")
# else:
#     print("Invalid number")

import re
N=input()
for i in range(N):

 if re.match(r'[789]\d{9}$',raw_input()):
    print ('YES')
 else:
    print ('NO')


