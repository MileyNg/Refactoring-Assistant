from itertools import combinations

while True:
    n, x = map(int, input().strip().split())
    if n == x == 0: break
    print(sum(1 for i in combinations(range(1, n + 1), 3) if sum(i) == x))