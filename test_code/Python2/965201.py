n = input()
for i in xrange(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, raw_input().split())
    Ax = x1 - x2
    Ay = y1 - y2
    Bx = x3 - x4
    By = y3 - y4
    if Ax == Bx == 0 or Ay == By == 0:
        print "YES"
    elif abs(Ay * Bx - By * Ax) < 1e-10:
        print "YES"
    else:
        print "NO"