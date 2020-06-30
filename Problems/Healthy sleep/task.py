least = int(input())
most = int(input())
ann = int(input())

if least <= ann <= most:
    print("Normal")
elif ann < least:
    print("Deficiency")
else:
    print("Excess")
