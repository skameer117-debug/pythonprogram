no=int(input())
s=0
for d in range(1,no//2+1,1):
	if no%d==0:
		s=s+d
if no==s:
	print(no," is a perfect number")
else:
	print(no," is not a perfect number")
		
	