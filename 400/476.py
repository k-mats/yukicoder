n, a = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

if sum(x) / n == a:
    print('YES')
else:
    print('NO')
