import pickle
f1=open("file1.txt","rb")
L=pickle.load(f1)
print(L)
f1.close()