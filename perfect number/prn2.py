for a in range(1,21,1):
	if a==0 or a==1:
		continue
	c=0
	for b in range(2,a//2+1,1):
		if a%b==0:
			c=c+1
	if c==0:
		print(a,"is a prime number")
	else:
		print(a,"is not a prime number")