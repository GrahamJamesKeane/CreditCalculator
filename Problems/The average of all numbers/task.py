a = int(input())
b = int(input())
sigma = 0
count = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        sigma += i
        count += 1

print(sigma / count)
