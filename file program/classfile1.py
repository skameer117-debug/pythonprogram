file handling
________________
store data secondary memory location then use file concept.
because ram is volatile.


There are 2 types of file
(1)text file
human readble format


(2)binary file
binary format

open(): it is function
open("filename","mode")

mode
_______
w     write  
a    
r
w+
a+
r+
wb
ab
rb
wb+
ab+
rb+


create blank file and close it
______________________________
f=open("sita.txt","w")
f.close()

write():it is used to write data into file.
it must be string type.
f=open("sita.txt","w")
f.write("hi")
f.write("bye")
#f.write(10)  error
#f.write(12.34) error
f.close()
o/p:




read(): :it is used to read data from file.
f=open("sita.txt","r")
print(f.read())
f.close()

o/p:
read all data from sita.txt file



f=open("sita.txt","r")
print(f.read(5))
f.close()

o/p:
it reads 5 char



f=open("sita.txt","r")
print(f.readline())
f.close()

o/P;
it read one line


f=open("sita.txt","r")
print(f.readlines())
f.close()
o/p:
['hi bye\n', 'ok\n', 'good night']



f=open("sita.txt","r")
L=f.readlines()
for i in L:
	print(i)
f.close()


o/p:
hi bye
ok
good night






copy one file to another file
_________________________________

f=open("sita.txt","r")
f1=open("gita.txt","w")
f1.write(f.read())
f.close()
f1.close()











open and closing single file
_______________________________
f=open("rita.txt","r")
print(f.read())
f.close()
f=open("rita.txt","a")
f.write("bye")
f.close()


random acess file
____________________
tell(): cursor which location
seek(): movement 
 
f=open("sita.txt","r")
print(f.tell())
f.seek(4)
print(f.read())
print(f.tell())
f.close()



C:\Users\HP\Desktop\python p>py 1.py
0
efghijklmnopqrstuvwxyz
26


f=open("sita.txt","r")
print(f.tell())
f.seek(4)
print(f.read(6))
print(f.tell())
f.seek(0)
print(f.read())
f.close()


o/p:
C:\Users\HP\Desktop\python p>py 1.py
0
efghij
10
abcdefghijklmnopqrstuvwxyz



f=open("sita.txt","r")
print(f.tell())
f.seek(4)
print(f.read(6))
print(f.tell())
f.seek(5)
print(f.read())
f.close()

o/p:
0
efghij
10
fghijklmnopqrstuvwxyz



f=open("sita.txt","r+")
print(f.read())
f.write("hello")
f.close()



f=open("sita.txt","w+")
f.write("defg")
f.seek(0)
print(f.read())
f.close()



f=open("sita.txt","a+")
f.write("defg")
f.seek(0)
print(f.read())
f.close()


How to Write data into a Binary File in Python | Writing data into a binary file using Python
To write an object  to a binary file opened in the write mode, we should use dump( ) function of pickle module as per the following syntax :

pickle.dump(<object>, <file-handler>)




import pickle
f1=open("file1.txt","wb")
list1=[1,'Lovejot','Teacher']
pickle.dump(list1,f1)
f1.close()



import pickle
f1=open("file1.txt","rb")
L=pickle.load(f1)
print(L)
f1.close()