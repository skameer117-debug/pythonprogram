s=0
for a in range(1,21,1):
	if a==0 or a==1:
		continue
	c=0
	for b in range(2,a//2+1,1):
		if a%b==0:
			c=c+1
	if c==0:
		s=s+a
		print(a,"is a prime number")
print("sum of prime number :",s)	