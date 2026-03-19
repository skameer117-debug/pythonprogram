sum=0
for no in range(1,1001,1):
	s=0
	for d in range(1,no//2+1,1):
		if no%d==0:
			s=s+d
	if no==s:
		sum=sum+no
		print(no," is a perfect number")
print("sum of perfect no=",sum)
		