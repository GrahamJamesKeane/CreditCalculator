x_coord = int(input())
y_coord = int(input())

if 1 < x_coord < 8 and 1 < y_coord < 8:
    print(8)
elif x_coord == 1 and y_coord == 8 or x_coord == 8 and y_coord == 1 or x_coord == y_coord == 1 or x_coord == y_coord == 8:
    print(3)
elif x_coord in (1, 8) and 1 < y_coord < 8 or y_coord in(1, 8) and 1 < x_coord < 8:
    print(5)
