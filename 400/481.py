b = [int(i) for i in input().split()]
b = set(b)
for i in range(1, 11):
    if i not in b:
        print(i)
        break
