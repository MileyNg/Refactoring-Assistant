N = 50000
t = [1]*(N)
p = [2]
d = {2:1}
for i in range(3, N, 2):
    if t[i]:
        p.append(i)
        d[i] = 1
        for j in range(3*i, N, 2*i): t[j] = 0

while True:
    n = int(input())
    if n == 0: break

    count = 0
    if n % 2:
        if n - 2 in p: count += 1
    else:
        for p1 in p:
            if 2*p1 > n: break
            if n - p1 in d:
                count += 1
    print(count)