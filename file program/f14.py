import pickle
f1=open("file1.txt","wb")
list1=[1,'Lovejot','Teacher']
pickle.dump(list1,f1)
f1.close()