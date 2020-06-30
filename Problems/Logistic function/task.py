from math import exp

num = int(input())

output = round((1 / (1 + exp(-num))), 2)
print(output)