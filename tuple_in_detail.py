# Both these declarations of tuple are identical
t1 = ('x','y')
print(type(t1))
t1 = 'x','y'
print(type(t1))
print()

# To store tuple items in individual variables, use multiple variables on the left of assignment operator
# This is called Unpacking of a tuple
tup1 =(10,20,30)
x,y,z =tup1
print("x: ", x, "y: ", y,"z: ", z)

'''
If the number of variables is more or less than the length of tuple, Python raises a ValueError.
In such a case, the "*" symbol is used for unpacking. Prefix "*" to "y", as shown below
The first value in tuple is assigned to "x", and rest of items to "y" which becomes a list.
'''
tup1 =(10,20,30)
x,*y =tup1
print("x: ", x, "y: ", y)

tup1 =(10,20,30,40,50,60)
x,*y,z =tup1
print("x: ",x,"y: ",y,"z: ",z)

tup1 =(10,20,30,40,50,60)
*x,y,z =tup1
print("x: ",x,"y: ",y,"z: ",z)
print()

#Looping
tup1 =(25,12,10,-21,10,100)
for num in tup1:
	print(num, end=' ') #end parameter of print() prints the string provided after each print is executed
print()
print()

# Joining Tuples
T1 =(10,20,30,40)
T2 =('one','two','three','four')
T3 =T1+T2 # same as T1+=T2
print("Joined Tuple:",T3)

# Using extend() method
# Convert the tuple to list first, then use entend() method, convert result back to tuple
T1 =(10,20,30,40)
T2 =('one','two','three','four')
L1 =list(T1)
L2 =list(T2)
L1.extend(L2)
T1 =tuple(L1)
print("Joined Tuple using extend():",T1)

'''
The elements of the first tuple are appended to an empty tuple first, 
and then elements from second tuple are appended and returns a new tuple that is concatenation of the two.
'''
T1 =(10,20,30,40)
T2 =('one','two','three','four')
T3 =sum((T1,T2),())
print("Joined Tuple using sum():",T3)

# A slightly complex approach for merging two tuples is using list comprehension, as following code shows −
T1 =(10,20,30,40)
T2 =('one','two','three','four')
L1,L2 =list(T1),list(T2)
L3 =[y for x in[L1,L2] for y in x]
T3 =tuple(L3)
print("Joined Tuple:",T3)

T1 =(10,20,30,40)
print('Tuple ID Before COncatenation', id(T1))
T2 =('one','two','three','four') 
for t in T2:
	T1+=(t,)
print(T1)
print('Tuple ID After Concatenation',id(T1))
print()

'''
Finding the Index of a Tuple Item
The index() method of tuple class returns the index of first occurrence of the given item.
'''
tup1 =(25,12,10,-21,10,100)
print("Tup1:",tup1)
x =tup1.index(10)
print("First index of 10:",x)
print()

# Counting in a Tuple
tup1 =(10,20,45,10,30,10,55)
print("Tup1:",tup1)
c =tup1.count(10)
print("count of 10:",c)

Tup1 =(10,20/80,0.25,10/40,30,10,55)
print("Tup1:",tup1)
c =Tup1.count(0.25)
print("count of 10:",c)
print()

# Python program to find unique numbers in a given tuple −
T1 =(1,9,1,6,3,4,5,1,1,2,5,6,7,8,9,2)
T2 =() 
for x in T1: 
	if x not in T2: 
		T2+=(x,)
print("original tuple:",T1)
print("Unique numbers:",T2)
print()

# Python program to find sum of all numbers in a tuple −

T1 =(1,9,1,6,3,4)
ttl =0 
for x in T1: 
	ttl+=x   
print("Sum of all numbers Using loop:",ttl)
ttl =sum(T1)
print("Sum of all numbers sum() function:",ttl)
print()

# Python program to create a tuple of 5 random integers −

import random
t1 =() 
for i in range(5):
	x =random.randint(0,100)
	t1+=(x,)
print(t1)
print()

'''
Tuple exercises
	• Python program to remove all duplicates numbers from a list.
	• Python program to sort a tuple of strings on the number of alphabets in each word.
	• Python program to prepare a tuple of non-numeric items from a given tuple.
	• Python program to create a tuple of integers representing each character in a string
	• Python program to find numbers common in two tuples.
'''
# Python program to remove all duplicates numbers from a list
t1 = ()
for i in range(20):
	x=random.randint(0,5)
	t1+=(x,)
print('Randomly created tuple: ',t1)
ut = ()
for i in t1:
	if i not in ut:
		ut+=(i,)
print('Unique numbers from randomly created tuple list: ',ut)
print()

# Python program to sort a tuple of strings on the number of alphabets in each word.
tstr = ('Python', 'program', 'to', 'sort', 'a', 'tuple', 'of', 'strings', 'on', 'the', 'number', 'of', 'alphabets', 'in', 'each', 'word')
print('Original Tuple: ', tstr)
lstr = list(tstr)
lstr.sort()
for i in range(0,len(lstr)-1):
  for j in range(i,len(lstr)):
    if (len(lstr[j])) < (len(lstr[i])):
      str1 = lstr[i]
      str2 = lstr[j]
      lstr.pop(i)
      lstr.insert(i, str2)
      lstr.pop(j)
      lstr.insert(j, str1)
'''
if (len(lstr[0])) <= (len(lstr[1])):
  str1 = lstr[0]
  str2 = lstr[1]
  print('Before Pop: ',lstr)
  lstr.pop(0)
  lstr.insert(0, str2)
  lstr.pop(1)
  lstr.insert(1, str1)
  print('After Pop: ', lstr)
'''
      
tstr = tuple(lstr)
print('Sorted Tuple: ', tstr)


