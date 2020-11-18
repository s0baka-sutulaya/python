import random
answer = []
a = [random.randrange(1, 500, 1) for i in range(10)]
for i in range(len(a) - 1):
    m = a[i]
    n = a[i + 1]
    if m > n:
        answer.append(m)

print(answer)
