# class Student:
#     amount = 0
#     def __init__(self, height=160, money=0):
#         self.height = height
#         self.money = money
#         Student.amount += 1
#
# nick = Student(money=200)
# andrew = Student()
# print(nick.money)
# # print(andrew.money)


# class Student:
#     print("hi")
#     def __init__(self):
#         self.height = 160
#         print(self)
#     def sleep(self):
#         print("sleep")
#
# first_student = Student()
# r_student = Student()
# first_student.sleep()


# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height+=height
#
# nick = Student()
# kate = Student(height=170)
# print(kate.height)
# print(nick.height)
# print("summer")
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)

class Student:
    def __init__(self, name=None):
        self.name = name
    def __str__(self):
        return f"I am a student. My name is {self.name}."

nick = Student(name="Nick")
ann = Student()
print(nick)
print(ann)