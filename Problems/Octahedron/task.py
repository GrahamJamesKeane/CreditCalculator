from math import sqrt

edge = float(input())
area = 2 * sqrt(3) * pow(edge, 2)
volume = (1 / 3) * sqrt(2) * pow(edge, 3)
print(f"{area:.2f} {volume:.2f}")
