import argparse
from math import log, ceil

parser = argparse.ArgumentParser(description="Credit Calculator Project")
parser.add_argument("--type", help="Indicates the type of payment")
parser.add_argument("--payment", type=float, help=" Monthly payment")
parser.add_argument("--principal", type=int, help="Credit principal")
parser.add_argument("--periods", type=int, help="Number of months and/or years needed to repay the credit")
parser.add_argument("--interest", type=float, help="Annual interest rate")
args = parser.parse_args()
error = "Incorrect parameters"
args_list = [args.type, args.payment, args.principal, args.periods, args.interest]


def overpayment(a, b, c):
    return (a * c) - b


def annuity(x):
    if args_list[2] is None:  # Calculate the principal
        args_list[2] = principal(args_list[1], args_list[3], args_list[4])
        print(overpayment(args_list[1], args_list[2], args_list[3]))
    elif args_list[3] is None:  # Calculate the period
        args_list[3] = period(args_list[1], args_list[2], args_list[4])
        print(overpayment(args_list[1], args_list[2], args_list[3]))
    elif args_list[1] is None:  # Calculate the annuity payment
        args_list[1] = annuity_payment(args_list[2], args_list[3], args_list[4])
        print(overpayment(args_list[1], args_list[2], args_list[3]))


def differentiated(x):
    p = args_list[2]
    n = args_list[3]
    i = args_list[4] / (12 * 100)
    total_payment = 0
    instance_payment = None
    for month in range(1, n + 1):
        instance_payment = ceil((p / n) + i * (p - ((p * (month - 1)) / n)))
        print(f"Month {month}: paid out {instance_payment}")
        total_payment += instance_payment
    print(f"Overpayment = {total_payment - p}")


def check_negative_values(a):
    return a[1] is not None and a[1] < 0.0 or a[2] is not None and a[2] < 0 or a[3] is not None and a[3] < 0 or a[4] \
           is not None and a[4] < 0.0


def check_length(x):
    count = 0
    for item in x:
        if item is None:
            count += 1
    if count > 1:
        return True
    else:
        return False


def period(a, b, c):
    monthly_payment = a
    credit_principal = b
    credit_interest = c
    i = credit_interest / (12 * 100)
    x = monthly_payment / (monthly_payment - i * credit_principal)
    n = ceil(log(x, 1 + i))
    if n < 12:
        print(f"You need {n} months to repay this credit!")
    else:
        years = n // 12
        months = n % 12
        if years > 1 and months > 1:
            print(f"You need {years} years and {months} months to repay this credit!")
        elif years > 1 and months == 1:
            print(f"You need {years} years and {months} month to repay this credit!")
        elif years > 1 and months == 0:
            print(f"You need {years} years to repay this credit!")
        elif years == 1 and months == 1:
            print(f"You need {years} year and {months} month to repay this credit!")
        elif years == 1 and months == 0:
            print(f"You need {years} years to repay this credit!")
    return n


def annuity_payment(a, b, c):
    credit_principal = a
    periods = b
    credit_interest = c
    i = credit_interest / (12 * 100)
    a_payment = ceil(credit_principal * (i * pow(1 + i, periods)) * (1 / (pow(1 + i, periods) - 1)))
    print(f"Your annuity payment = {a_payment}!")
    return a_payment


def principal(a, b, c):
    payment = a
    periods = b
    interest = c
    i = interest / (12 * 100)
    credit_principal = payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
    print(f"Your credit principal = {credit_principal}!")
    return credit_principal


if args.type not in ["annuity", "diff"] or check_length(args_list) or check_negative_values(args_list):
    print(error)
    exit(0)
elif args.type == "diff" and args.payment is not None or args.type == "annuity" and args.interest is None:
    print(error)
    exit(0)
else:
    if args.type == "annuity":
        annuity(args_list)
    elif args.type == "diff":
        differentiated(args_list)
