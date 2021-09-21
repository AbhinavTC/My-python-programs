# class complex():
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def add(self,number):
#         real=self.real+number.real
#         img=self.img+number.img
#         result=complex(real,img)
#         return result
#
# n1=complex(5,6)
# n2=complex(-4,2)
# result=n1.add(n2)
# print("real=",result.real)
# print("img=",result.img)

# num=[1,3,4,5,7]
# print(dir(num))

# def my_function():
#     pass
# print(type(my_function))

# number = 5
# number2 = 7
# print(id(number))
# print(id(number2))
# number = number2
# print(id(number))


# class eli():
#     def __init__(self,height,weight):
#         self.height=height
#         self.weight=weight
#
#     def did_select(self):
#         if self.height>=180:
#             print("selected")
#         else:
#             print("Rejecetd")
#
# aspire1 = eli(181,45)
# selected = aspire1.did_select()
# print(selected)


# class Triangle():
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def tprimeter(self):
#         perimeter = self.a + self.b + self.c
#         return perimeter
#
#
# T1 = Triangle(3, 7, 5)
# perimeter = T1.tprimeter()
# print("The perimeter of the triangle =", perimeter)

#inheritance
#
# class Animal:
#     def eat(self):
#         print("I can eat")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("I can bark")
#
#
# class Cat(Animal):
#     def get_grumpy(self):
#         print("I am getting grumpy.")
#
#
# dog1 = Dog()
#
# dog1.bark()
# dog1.eat()
#
# cat1 = Cat()
# cat1.eat()


