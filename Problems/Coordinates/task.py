x_coord = float(input())
y_coord = float(input())

if x_coord > 0 and y_coord > 0:
    print("I")
elif y_coord < 0 < x_coord:
    print("IV")
elif x_coord < 0 and y_coord < 0:
    print("III")
elif x_coord < 0 < y_coord:
    print("II")
