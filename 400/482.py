n, k = [int(i) for i in input().split()]
d = [int(i) - 1 for i in input().split()]

e = [0 for i in range(n)]
for i, d_i in enumerate(d):
    e[d_i] = i

used_indices = set()
swap_times = list()

for i in range(n):
    index = i
    swap_time = -1

    while index not in used_indices:
        used_indices.add(index)
        index = e[index]
        swap_time += 1

    if swap_time > 0:
        swap_times.append(swap_time)

total_swap_time = sum(swap_times)

if (k - total_swap_time) % 2 == 0 and k >= total_swap_time:
    print('YES')
else:
    print('NO')
