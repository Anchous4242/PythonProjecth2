# try:
#     print("start code")
#     # print(dfgh)
#     print(10/0)
#     print("No errors")
# # except:
# #     print("ooops error")
# except NameError:
#     print(" NAME ERROR!!!")
# except ZeroDivisionError:
#     print("ZeroDivision ERROR!!!")
# print("after capsule")
#
# try:
#     print("start")
#     # print(start)
#     print("No errors")
# except (SyntaxError,NameError) as error:
#     print(error)
#     print()
# else:
#     print("I am ELSE")
# finally:
#     print("Finally code")
#
#     try:
#         print("start")
#         # print(start)
#         print("No errors")
#     except (SyntaxError, NameError) as error:
#         print(error)
#         print()
#     else:
#         print("I am ELSE")
#     finally:
#         print("Finally code")


class BuildingEror(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"


def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        print("enough material")
    else:
        raise BuildingEror(amount_of_material)


materials = 120
try:

    check_material(materials, 150)
except BuildingEror as error:
     print(error)