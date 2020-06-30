phone_number_str = list(input())
phone_number_int = []
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for digit in phone_number_str:
    phone_number_int.append(int(digit))

for digit in phone_number_int:
    print(digits[digit])
