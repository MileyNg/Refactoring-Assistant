for i in range(int(raw_input())):
    s = raw_input()
    for a in range(1, 1000):
        for b in range(26):
            def f(s, a, b):
                return ''.join([chr(((ord(c) - ord('a')) * a + b) % 26 + ord('a')) for c in s])
            if f('that', a, b) in s or f('this', a, b) in s:
                dic = dict([(chr((i * a + b) % 26 + ord('a')), chr(i + ord('a'))) for i in range(26)])
                print ''.join([dic.get(c, c) for c in s])
                break
        else:
            continue
        break