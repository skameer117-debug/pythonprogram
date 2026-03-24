s="ram is a good boy"
s1=""
if ord(s[0])>=97 and ord(s[0])<=122:
	s1=s1+chr(ord(s[0])-32)
i=1
while i<len(s):
	if s[i]==' ':
		s1=s1+" "
		if ord(s[i+1])>=97 and ord(s[i+1])<=122:
			s1=s1+chr(ord(s[i+1])-32)
		else:
			s1=s1+s[i+1]
		i=i+1
	else:
		s1=s1+s[i]
	i=i+1
print(s1)