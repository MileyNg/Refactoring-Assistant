n = int(raw_input())
taro=hana=0
for i in xrange(n):
	x,y=map(str,raw_input().split())
	if x == y:
		taro += 1
		hana += 1
	elif x < y:
		hana += 3
	else:
		taro += 3
print "%d %d" % (taro,hana)