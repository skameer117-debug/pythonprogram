no=145
str=0
temp=no
while temp>0:
	r=temp%10
	f=1
	while r>0:
		f=f*r
		r=r-1
	str=str+f
	temp=temp//10
if no==str:
	print(no," is strong number")
else:
	print(no," is not strong")