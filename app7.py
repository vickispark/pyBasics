print("calculator::python default converts user input to string so apply float on user num input")
num1 = float(input("giv num1:"))
op = input("giv operator")
num2 = float(input("giv num2:"))

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("invalid operator")
