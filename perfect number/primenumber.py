no=11
c=0
for d in range(2,no//2+1,1):
	if no%d==0:
		c=c+1
if c==0:
	print(no,"is a prime number")
else:
	print(no,"is not a prime number")