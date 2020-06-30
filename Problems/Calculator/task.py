# put your python code here
num_1 = float(input())
num_2 = float(input())
operation = input()
error = "Division by 0!"


def check_num(a):
    return a == 0


if operation == "+":
    print(num_1 + num_2)
elif operation == "-":
    print(num_1 - num_2)
elif operation == "/":
    print(num_1 / num_2 if not check_num(num_2) else error)
elif operation == "*":
    print(num_1 * num_2)
elif operation == "mod":
    print(num_1 % num_2 if not check_num(num_2) else error)
elif operation == "div":
    print(num_1 // num_2 if not check_num(num_2) else error)
elif operation == "pow":
    print(num_1 ** num_2)
