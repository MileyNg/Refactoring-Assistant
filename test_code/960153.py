n = int(input())
cards = []
for i in range(n):
    s, r = input().strip().split()
    cards.append((s, int(r)))
for s, r in [(s, r) for s in 'SHCD' for r in range(1, 14) if (s, r) not in cards]:
    print(s, r)