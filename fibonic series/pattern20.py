c=1
c1=0
for i in range(1,5,1):
	c1=c+i
	for j in range(1,i+1,1):
		if i%2==0:
			c1=c1-1
			print(c1,end="\t")
		else:
			print(c,end="\t")
		c=c+1
	print()