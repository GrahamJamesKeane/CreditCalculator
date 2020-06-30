cash = int(input())
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

if cash >= sheep:
    print(str(cash // sheep) + " " + "sheep")
elif cash >= cow:
    print(str(cash // cow) + " " + "cows" if cash // cow > 1 else str(cash // cow) + " " + "cow")
elif cash >= pig:
    print(str(cash // pig) + " " + "pigs" if cash // pig > 1 else str(cash // pig) + " " + "pig")
elif cash >= goat:
    print(str(cash // goat) + " " + "goats" if cash // goat > 1 else str(cash // goat) + " " + "goat")
elif cash >= chicken:
    print(str(cash // chicken) + " " + "chickens" if cash // chicken > 1 else str(cash // chicken) + " " + "chicken")
else:
    print("None")
