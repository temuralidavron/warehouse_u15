#
#
# class Person:
#     __slots__=('username','age')  # objlarni atributlarnini nazorat qilish uchun kerak
#     def __init__(self,username,age):
#         self.username=username
#         self.age=age
#
#
#
#
# obj=Person('ali',20)
#
#
#
# class Student(Person):
#     __slots__ = ('level',)
#     def __init__(self,username,age,level):
#         super().__init__(username,age)
#         self.level=level
#
#
# std=Student("vali",20,1)
# print(std)