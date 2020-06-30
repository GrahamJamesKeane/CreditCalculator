from math import log

num1 = int(input())
num2 = int(input())

if num2 <= 1:
    output = round(log(num1), 2)
    print(output)
else:
    output = round(log(num1, num2), 2)
    print(output)
