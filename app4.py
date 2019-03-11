print("a tuple is similar to list but also different,paranthesis used to represent \n \
 tuple immutable i.e cant modify \n \
 tuples mostly used for constants,coordinates etc..")
cord = (3,4)
print(cord[0])
print("functions use keyword def,leave 2 blank lines before and after funct")


def greet():
    print("HEY")


def func_1(name,age) :
    print(name+str(age))
    print("indent inside func1")


def cube(num):
    return num*num*num


greet()
func_1("HELLO",1)
func_1("HELLO",2)
res = cube(4)
print(res)
print("return statement is last line of function def")








