while 1:
	n=input()
	if n==0:break
	p=[0]*n
	l=[[0]*31 for i in range(n)]
	a=sorted([raw_input().split() for i in range(n)])
	for j in range(n):
		for t in a[j][2:]:
			l[j][int(t)]=1
	for t in range(30):
		c=0
		for j in range(n):
			if l[j][t]:c+=1
		for j in range(n):
			if l[j][t]:p[j]+=n-c+1
	print min(p),a[p.index(min(p))][0]