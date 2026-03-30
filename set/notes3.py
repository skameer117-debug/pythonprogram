tuple
______


tuple is  a immutable
it is collection of simliar or dismliar type of elements.
insertion order preserved
index and slicing concept avilable 
tuple  comphersnion not allow

we can represent tuple by using ()  

t=10
print(type(t))

o/p:
<class int>

t=10,20
print(type(t))

o/p:
<class tuple>


t=(10)
print(type(t))

o/P:
<class int>


t=(10,)
print(type(t))

o/p:
<class tuple>


tuple is immutably
________________________
t1=(10,20,30)
t2=(10,20,30)
print(id(t1),id(t2))


o/p:
2804492125440 2804492125440


   


L=[10,20,30]
t=tuple(L)
t1=tuple("hi")
print(t,t1)

o/p:
(10, 20, 30) ('h', 'i')


indexing and slicing concept avaliable
__________________________________________
t=(5,8,12,3,8)
print(t[1],t[-4])
print(t[2:4:1])


o/p:
8 8
(12, 3)










take input from keyboad and display it
____________________________________
print("enter tuple data")
t=eval(input())
print(t)

o/p:
enter tuple data
10,20,12.34
(10, 20, 12.34)



operator
___________________--
t=(5,8,12)
print(12 in t)
print(7 in t)
print(7 not in t)
t1=(5,8,12)
t2=(5,9,12)
print(t==t1)
print(t is t1)
print(t1>t2)
print(t1>=t2)
print(t1<t2)
print(t1<=t2)
#print(t+3) error
print(t1+t2)
print(t1*3)
o/p
True
False
True
True
True
False
False
True
True
(5, 8, 12, 5, 9, 12)
(5, 8, 12, 5, 8, 12, 5, 8, 12)


//dispaly tuple element
t=(5,8,12,23)
for i in t:
    print(i)
o/p:
5
8
12
23




t=(5,8,12,23)
for i in range(0,len(t),1):
    print(t[i])
o/p:
5
8
12
23


t=(5,8,12,23)
t[2]=30   # error  immutable
print(t)




t=(5,8,12,23,8)
print(t.count(8))

o/p:
2


t=(5,8,12,23,8)
print(t.index(8))
print(t.index(8,0))
print(t.index(8,2))
o/p:
1
1
4

sort element
t=(5,8,7,4)
L=list(t)
L.sort()
t=tuple(L)
print(t)

o/p:
(4, 5, 7, 8)





set
_____________
it is another datastructute.

insertion order is not preserved.


duplicate element not allow

indexing and slicing  concept not avaliable

using { } create set


s={ }
print(type(s))

o/p:
dict


s={7}
print(type(s))

o/p:
set







s={7,8,12,7,9,8}
print(s)
o/p:
{8, 9, 12, 7}

s=set()
print(s)
o/p:
set




L=[3,5,3,7,5,8]
s=set(L)
print(s)
o/P:
{8,3,5,7}



s1={5,8,7}
for i in s1:
    print(i)



take input and dispaly it

print("enter set data ")
s1=eval(input())
for i in s1:
    print(i)

o/p:
enter set data
{3,5,4,3,8,7,3}
3
4
5
7
8





s1={3,5,8,9}
s2={5,4,9,10}
print(s1|s2)
print(s1.union(s2))
print(s1)
print(s2)

o/p:
C:\Users\HP\Desktop\python8pm>py add.py
{3, 4, 5, 8, 9, 10}
{3, 4, 5, 8, 9, 10}
{8, 9, 3, 5}
{9, 10, 4, 5}



s1={3,8,9,5}
s2={5,4,9,10}
s1.update(s2)
print(s1)
print(s2)


o/p:
{3, 4, 5, 8, 9, 10}
{9, 10, 4, 5}




s1={3,5,8,9}
s2={5,4,9,10}
print(s1.intersection(s2))
print(s1&s2)
print(s1)
print(s2)
s1.intersection_update(s2)
print(s1)
print(s2)

o/p:
{9, 5}
{9, 5}
{8, 9, 3, 5}
{9, 10, 4, 5}
{9, 5}
{9, 10, 4, 5}


union
update 
intersection
intersection_update




s1={3,5,8,9}
s2={5,4,9,10}
print(s1.difference(s2))
print(s1-s2)
print(s1)
print(s2)
s1.difference_update(s2)
print(s1)
print(s2)
o/p:
{8, 3}
{8, 3}
{8, 9, 3, 5}
{9, 10, 4, 5}
{3, 8}
{9, 10, 4, 5}



s1={3,5,8,9}
s2={5,4,9,10}
print(s1.symmetric_difference(s2)) 
print(s1^s2)
print(s1)
print(s2)
s1.symmetric_difference_update(s2)
print(s1)
print(s2)


o/p:
{3, 4, 8, 10}
{3, 4, 8, 10}
{8, 9, 3, 5}
{9, 10, 4, 5}
{3, 4, 8, 10}
{9, 10, 4, 5}



add element in set
____________________
s1={3,5,8,9}
s1.add(17)
print(s1)


o/p:
{3, 5, 8, 9, 17}







s1={3,5,8,9}
s1.remove(8)
print(s1)

o/p:
{9 3 5}


s1={3,5,8,9}
s1.remove(12)
print(s1)

o/p:
error

keyerror




s1={3,5,8,9}
s1.discard(8)
print(s1)

o/p:
{9,3,5}



s1={3,5,8,9}
s1.discard(12)
print(s1)

o/p:
{8, 9, 3, 5}



s1={3,5,8,9}
s1.pop()
print(s1)

o/p:
{9, 3, 5}

s1={3,5,8,9}
s1.clear()
print(s1)


o/P:
set()


s1={3,5}
print(s1.issubset({5,4,3}))
print(s1.issuperset({5,4,3}))
print({10,2,3,5}.issuperset(s1))

o/p:
True
False
True



s1={3,5}
s2=s1 
s2.add(7)
print(s1)
print(s2)


o/p:
{3, 5, 7}
{3, 5, 7}




s1={3,5}
s2=s1.copy() 
s2.add(7)
print(s1)
print(s2)

o/p:
{3, 5}
{3, 5, 7}


s1={3,5}
s2={4,7} 
print(s1.isdisjoint(s2))

o/p:
True
_________________________________




set compershinon
_________________________
s={i for i in "hello"}
print(s)
o/p:
{'h', 'e', 'o', 'l'}



s={i+3 for i in [2,3,4,7,8,4,7,5,5] if i%2==0}
print(s)


o/p:
{11, 5, 7}

https://chatgpt.com/share/686d3fda-75c4-8008-9553-67b246900813
https://chatgpt.com/share/68949ddd-fd44-8008-9f2c-b8af002f3eaa



tuple comphersion  not avaliable
__________________________________