print("enter salary")
sal=float(input())
if sal>=5000:
	da=sal*0.7
	hra=sal*0.5
else:
	da=sal*0.4
	hra=sal*0.3
total=sal+da+hra
print ("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total=",total)