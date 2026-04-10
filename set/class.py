print("A")
print("B")
print("C")
print("A")
print("B")
print("C")
print("A")
print("B")
print("C")

some statement repeated continously then choose loop concept 

benifits of loop
_________________
write that repeated stmt only once inside the loop body.


for i in range(3):
	print("A")
	print("B")
	print("C")


print("A")
print("B")
print("C")
print("D")
print("A")
print("B")
print("C")
print("E")
print("A")
print("B")
print("C")
print("F")

some statement repeated after sometime then choose function concept 

How to define function
________________________


def  functionname(formal parameter,...):
	function body logic
	return


How to function call
________________________

functionname(actual parameter)


def show():
	print("A")
	print("B")
	print("C")
show()
print("D")
show()
print("E")
show()
print("F")



we can write function program 4 way
_____________________________________
(1)no return value no argument
(2)no returnvalue with argument
(3)return value with no argument
(4)return value with argument




#add two number  without function

print("enter a number ")
no1=int(input())
print("enter another number ")
no2=int(input())
s=no1+no2
print("sum=",s)


(1)no return value no argument   add two number 

def add():
	print("enter a number ")
	no1=int(input())
	print("enter another number ")
	no2=int(input())
	s=no1+no2
	print("sum=",s)
	return
add()



(2)no return value with argument   add two number 

def add(no1,no2):
	s=no1+no2
	print("sum=",s)
	return
print("enter a number ")
no1=int(input())
print("enter another number ")
no2=int(input())
add(no1,no2)



(3)return value with no argument   add two number 

def add():
	print("enter a number ")
	no1=int(input())
	print("enter another number ")
	no2=int(input())
	s=no1+no2
	return s
res=add()
print("sum=",res)


(4)return value with argument   add two number 

def add(no1,no2):
	s=no1+no2
	return s
print("enter a number ")
no1=int(input())
print("enter another number ")
no2=int(input())
res=add(no1,no2)
print("sum=",res)

---------------------------------------------------------------------------------------

Types of parameter
_______

(1)requried parameter
(2)default parameter
(3)keyword parameter
(4)variable length parameter


requried parameter
______
def show(a,b,c,d):
	print(a,b,c,d)

show(10,12.34,"hi",5)
#show(1,5,7) error

o/p:
10 12.34 hi 5



default parameter
______

def  show(a=0,b=0,c=10,d=0):
	print(a,b,c,d)
show(5,"hi")
show(1,5,7,12.34)
show()

o/p:
5 hi 10 0
1 5 7 12.34
0 0 0 0



keyword parameter
______

def  show(a=0,b=3,c=10,d=0):
	print(a,b,c,d)
show(1,5,7,12.34)
show(d=25,c=12,a=5,b=1)
show(c=30)
o/p:
1 5  7  12.34
5 1  12  25
0 3 30 0



variable length parameter
_________
1. *args (Variable-Length Positional Arguments)
The *args syntax allows a function to accept any number of positional arguments. Inside the function, args is treated as a tuple.

def show(*a):
	print(a)
show(10,12.34)
show("hi",1,5.3)

o/p:
(10, 12.34)
('hi', 1, 5.3)


 result

# Calling with a varying number of arguments
print(multiply(2, 3))          # Output: 6
print(multiply(2, 3, 4))       # Output: 24
print(multiply(1, 2, 3, 4, 5)) # Output: 120







def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling with varying keyword arguments
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
print_info(brand="Toyota", model="Corolla", year=2020)
# Output:
# brand: Toyota
# model: Corolla
# year: 2020



def show(*a,b):
	print(a)
show(10,12.34)
show("hi",1,5.3)

o/p:
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\demo.py", line 3, in <module>
    show(10,12.34)
TypeError: show() missing 1 required keyword-only argument: 'b'



def show(b,*a):
	print(a)
show(10,12.34,"hi")
show("bye",1,5.3)
o/p:
(12.34, 'hi')
(1, 5.3)



Combining *args and **kwargs
You can use both *args and **kwargs in the same function. However, *args must come before **kwargs in the function definition.

Example:
def display(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling with both positional and keyword arguments
display(1, 2, 3, name="Alice", age=30)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}






______________________________________________
✅ (1) Required Parameter (Positional Parameter)
📘 Theory:
These are mandatory parameters in a function. You must pass values in the correct order. If any required parameter is missing, Python will raise an error.

def add(a, b):
    print("Sum =", a + b)

add(10, 20)     # Correct
# add(10)       # ❌ Error: Missing required argument 'b'
✅ Key Point:
Order matters.

Cannot be skipped.

✅ (2) Default Parameter
📘 Theory:
You can assign a default value to a parameter. If no value is passed, the default is used. If you pass a value, it overrides the default.

def greet(name, msg="Good Morning"):
    print("Hello", name, "-", msg)

greet("Alice")                  # Uses default message
greet("Bob", "Good Evening")   # Overrides default
✅ Key Point:
Must be at the end of the parameter list.

Used to make parameters optional.

✅ (3) Keyword Parameter
📘 Theory:
You pass the argument by name, not by position. This makes your code more readable and the order of arguments doesn't matter.


def student(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student(age=18, grade="A", name="Rita")  # Order doesn't matter
✅ Key Point:
Improves code clarity.

Useful when there are many parameters.

✅ (4) Variable Length Parameter
Python supports two types of variable-length parameters:

🔹 (a) *args → for variable positional arguments
📘 Theory:
Allows passing any number of positional arguments. It stores them as a tuple.


def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(85, 90)
total_marks(70, 80, 90, 95)
🔹 (b) **kwargs → for variable keyword arguments
📘 Theory:
Allows passing any number of keyword arguments. It stores them as a dictionary.


def profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

profile(name="John", age=22, city="Delhi")
🎯 Summary Table:
Type                 Syntax  Use Case                               Stored As
Required Parameter  a, b        Must be passed in order                 Direct values
Default Parameter   a=10       Optional; use default if not passed       Direct values
Keyword Parameter   name="John" Pass by name for readability          Direct values
Variable-length (*args) *args   Pass many positional values            Tuple
Variable-length (**kwargs)  **kwargs    Pass many keyword values    Dictionary

-------------------------------------------------------------------------------------



local  variable    vs global variable
_________________________________________

local  variable :
A variable defined  inside function that is known as local variable .
That is visible within that function.
not access other function

def show():
	a=10 #local variable
	print("local ",a)
def disp():
	#print(a) error
	print("hi")


show()
disp()
#print(a)
o/p:
local 10
hi










global  variable:
A variable defined outside function that is known as global.
that can acees  all function


a=10 #global variable
def show():
	print("global ",a)
def disp():
	print(a)
	print("hi")
show()
disp()
print(a)

o/p:
global 10
10
hi
10



def show():
	print("global ",a)
def disp():
	print(a)
	print("hi")
a=10 #global varible
show()
disp()
print(a)

o/p:
global 10
10
hi
10



a=10 #global
def show():
	a=30 #local
	print("local ",a)
def disp():
	print(a)
	print("hi")
show()
disp()
print(a)

o/p:
local  30
10
hi
10


a=10
def show():
	global a
	a=30
	print(a) #global a display
def disp():
	print(a)
	print("hi")
show()
disp()
print(a)


o/p:
30
30
hi
30




a=10
def show():
	a=30
	print(a) #local 30
	print(locals()['a'])#local 30
	print(globals()['a']) #global 10
	globals()['a']=40	
show()
print(a)

o/p:
30
30
10
40




amount=10000
def deposit(amt):
	global amount
	amount=amount+amt 
	print(amt,"deposit")
def withdraw(amt):
	global amount 
	amount=amount-amt 
	print(amt,"withdraw")
print("balance=",amount)
deposit(3000)
withdraw(6000)
print("balance=",amount)


o/p:
balance= 10000
3000 deposit
6000 withdraw
balance= 7000


-------------------------------------------------------------------------------------------



call by value or call by refernce
___________________________________
call by value (value send)  int,float complex string tuple
def update(a):
	print(a)
	a=20

a=10
update(a)
print(a)

o/p:
10
10

call by address(reference send) list set dict
def update(L):
	print(L)
	L.append(40)
L=[10,20,30]
update(L)
print(L)
[10, 20, 30]
[10,20,30,40]
 

function alias
_________________
def show():
	print("show function")
s=show
d=s
show()
s()
d()




lambda function
_____________________

without lambda  find the square
__________________________
def  sq(x):
	y=x*x
	return y
res=sq(5)  #res variable
print(res)


lambda function 
__________________

lambda parameter: expression


res=lambda x:x*x   #res function
print(res(5))




without lambda function
_________________________

def add(x,y):
	return x+y 
res=add(10,20)
print(res)


using lambda
_________________

res=lambda x,y:x+y
print(res(2,3))


module 
___________
it is a python file.
it is collection of function,variable and class



There are 2 types of module.
(1)predefiend module
	sys,random,......
(2)userdefined module
	name must be valid identifier

How to access module in other file
___________________________________
(1)import modulename
(2)import modulename as dupname
(3)from modulename import membername,...
(4)from modulename importdef show():
	print("show function")
def add(no1,no2):
	return no1+no2
x=20 *;
mymod.py
__________________



1.py
_________
import mymod
mymod.show()
print(mymod.add(10,20))
print(mymod.x)

2.py
_________
import mymod as m
m.show()
print(m.add(10,20))
print(m.x)


3.py
________
from mymod import show,add,x
show()
print(add(10,20))
print(x)


4.py
_________
00



show function
30
20

predefined module math use
_________________________
import math
print(math.pi)
print(math.pow(2,3))
print(math.sqrt(16))

3.141592653589793
8.0
4.0


import math as m
print(m.pi)
print(m.pow(2,3))
print(m.sqrt(16))


from math import pi,pow,sqrt
print(pi)
print(pow(2,3))
print(sqrt(16))


from math import *
print(pi)
print(pow(2,3))
print(sqrt(16))



import random as r
print(r.random())
print(round(12.3456,2))
print(round(r.random(),3))

C:\Users\HP\Desktop\pythonpro>py 2.py
0.07210318327459808
12.35
0.787

C:\Users\HP\Desktop\pythonpro>py 2.py
0.22951788312383603
12.35
0.002


import random as r
print(r.uniform(10,20))

C:\Users\HP\Desktop\pythonpro>py 2.py
18.98421799815529
C:\Users\HP\Desktop\pythonpro>py 2.py
19.141364192175452

import random as r
print(r.randrange(10,20))  #any whole number  10 to 20


import random as r
print(r.choice("welcome"))
print(r.choice([4,6,12,45,7]))

C:\Users\HP\Desktop\pythonpro>py 2.py
l
4

C:\Users\HP\Desktop\pythonpro>py 2.py
m
4

C:\Users\HP\Desktop\pythonpro>py 2.py
m
6

import random as r
print(r.sample("welcome",3))
print(r.sample([4,6,12,45,7],4))
C:\Users\HP\Desktop\pythonpro>py 2.py
['w', 'c', 'e']
[4, 45, 6, 7]

C:\Users\HP\Desktop\pythonpro>py 2.py
['c', 'e', 'm']
[12, 6, 45, 7]



-------------------------------------------------------------------------------------------



recursion:
_________

A function call itself is known as recursion.
which program solve in loop that program solve using recursion.


without recursion
____________________

def show():
	print("hi")
print("A")
show()
print("B")

o/p:
A
hi
B


def show():
	print("hi")
	print("bye")
print("A")
show()
print("B")
o/p:
A
hi
bye
B




recursion
_____________
def show():
	print("hi")
	show()
	print("bye")
print("A")
show()
print("B")

o/p:
A
hi
hi
hi
.
.
.



i=1
def show():
	global i
	print("hi")
	i=i+1
	if(i<=3):
		show()
	print("bye")
print("A")
show()
print("B")

o/p:
A
hi
hi
hi
bye
bye
bye
B


def show(i):
	print("hi")
	if(i<=3):
		show(i+1)
	print("bye")
print("A")
show(1)
print("B")

o/p:
A
hi
hi
hi
hi
bye
bye
bye
bye
B


display 1 to 10 using recursion
_________________
def show(i):
	print(i)
	if(i<=9):
		show(i+1)
show(1)

o/p:
1
2
3
4
5
6
7
8
9
10


display 10 to 1 using recursion
_________________________________
def show(i):
	if(i<=9):
		show(i+1)
	print(i)
show(1)


o/p:
10
9
8
7
6
5
4
3
2
1



def show(i):
	print(i)
	if(i>0):
		show(i-1)	
show(10)

o/p:
10
9
8
7
6
5
4
3
2
1

factorial using function
_______________________
def fact(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
res=fact(4)
print("factorial=",res)


factorial using recursion
f=1
def fact(no):
	global f
	if no>0:
		f=f*no
		no=no-1
		fact(no)
	return f
res=fact(4)
print("factorial=",res)


or
factorial number  using recursion
def fact(no):
	if no==0:
		return 1
	else:
		return no*fact(no-1)
res=fact(4)
print("factorial=",res)



sum of digit recursion


s=0
def sdtest(no):
	global s
	if no!=0:
		s=s+no%10
		no=no//10
		sdtest(no)
	return s
res=sdtest(125)
print("sumof dgit=",res)



or

def sum_of_digits(n):
    # Base case: when n is reduced to a single digit
    if n == 0:
        return 0
    else:
        # Recursive case: last digit + sum of remaining digits
        return (n % 10) + sum_of_digits(n // 10)

# Test the function
number = int(input("Enter a number: "))
print(f"The sum of the digits of {number} is: {sum_of_digits(number)}")





revser number

_____________


def reverse_number(n, rev=0):
    # Base case: when n becomes 0, return the reversed number
    if n == 0:
        return rev
    else:
        # Recursive case: shift current rev by 1 digit and add the last digit of n
        return reverse_number(n // 10, rev * 10 + n % 10)

# Test the function
number = int(input("Enter a number: "))
reversed_num = reverse_number(number)
print(f"The reverse of {number} is: {reversed_num}")






Explanation:
Base Case: When the number n becomes 0, the recursion stops and returns the reversed number.
Recursive Case:
n % 10 extracts the last digit of the number.
rev * 10 shifts the reversed number to the left by one digit to make space for the next digit.
n // 10 removes the last digit of the number for the next recursive call.
Example:
For input 1234:


reverse_number(1234) => reverse_number(123, 4)
reverse_number(123) => reverse_number(12, 43)
reverse_number(12) => reverse_number(1, 432)
reverse_number(1) => reverse_number(0, 4321)
Thus, the reverse of 1234 is 4321.


----------------------------------------------------------------------------------------------



module:
it is a python file.
it contains function variable class
(a)predefined module
sys random  math numpy panda ,...
(b)userdefined module
that name must be valid identifier

how to use  module
______________________
(1)import  modulename
(2)import modulename as duplicatename
(3)from modulename import member,member,..
(4)from modulename import *
mymoduletest.py
__________________
def add(no1,no2):
	return no1+no2
def show():
	print("hi")
a=10

m1.py
___________
import mymoduletest
mymoduletest.show()
print(mymoduletest.add(10,20))
print(mymoduletest.a)
m2.py
__________
import mymoduletest as m
m.show()
print(m.add(10,20))
print(m.a)

m3.py
_______
from mymoduletest import show,add,a
show()
print(add(10,20))
print(a)

m4.py
_______
from mymoduletest import *
show()
print(add(10,20))
print(a)

package
__________
it is collection of  realted modules and subpackage.

every package is folder.
every folder is not package.

every package and subpackage inside __init__.py file /
it is blank file


moduleprogram->pk->__init__.py 
				  mymath.py
def add(no1,no2):
	return no1+no2
def sub(no1,no2):
	return no1-no2

moduleprogram->pk1->access mymath.py
                  m1.py
import pk.mymath as m
print(m.add(20,10))
print(m.sub(30,5))    

C:\Users\LENOVO\OneDrive\Desktop\c\nissfullstackpython\pythonniss\moduleprogram\pk1>set pythonpath=C:\Users\LENOVO\OneDrive\Desktop\c\nissfullstackpython\pythonniss\moduleprogram\

C:\Users\LENOVO\OneDrive\Desktop\c\nissfullstackpython\pythonniss\moduleprogram\pk1>py m1.py
30
25
m2.py
import pk.mymath
print(pk.mymath.add(20,10))
print(pk.mymath.sub(30,5))

                 
                  m3.py
from pk.mymath import add,sub
print(pk.mymath.add(20,10))
print(pk.mymath.sub(30,5))
                  m4.py
from pk.mymath import *
print(pk.mymath.add(20,10))
print(pk.mymath.sub(30,5))