dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
while True:
    ans = 0
    try:
        m = ['0'*14] + ['0'+raw_input()+'0' for i in xrange(12)] + ['0'*14]
        f = [[False for i in xrange(14)] for j in xrange(14)]
        for y in xrange(1, 13):
            for x in xrange(1, 13):
                if m[y][x]=='1' and f[y][x]==False:
                    q = [[x, y]]
                    f[y][x] = True
                    while len(q)>0:
                        px, py = q.pop(0)
                        for k in xrange(4):
                            nx = px + dx[k]; ny = py + dy[k];
                            if m[ny][nx]=='1' and f[ny][nx]==False:
                                f[ny][nx] = True
                                q.append([nx, ny])
                    ans += 1
        print ans
        raw_input()
    except EOFError:
        break