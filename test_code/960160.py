while True:
    m, f, r = map(int, input().strip().split())
    if m == f == r == -1: break
    if m == -1 or f == -1 or m + f < 30:
        print('F')
    elif m + f >= 80:
        print('A')
    elif m + f >= 65:
        print('B')
    elif m + f >= 50:
        print('C')
    elif m + f >= 30:
        print('C' if r >= 50 else 'D')