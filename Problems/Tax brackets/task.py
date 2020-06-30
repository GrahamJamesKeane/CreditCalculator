income = int(input())


def find_tax(value):
    if value >= 132407:
        return 28
    elif value >= 42708:
        return 25
    elif value >= 15528:
        return 15
    else:
        return 0


percent = find_tax(income)


def find_amount(a, b):
    return round((b / 100) * a)


calculated_tax = find_amount(percent, income)

print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
