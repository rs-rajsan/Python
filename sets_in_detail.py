'''
Objects in the assignment is not necessarily retained in the set object. 
This is because Python optimizes the structure of set for set operations.
'''
s1 ={"Rohan","Physics",21,69.75}
s2 ={5,3,4,2,1}
s3 ={"z","r","a","s"}
s4 ={25.50,True,-55,1+2j}
print(s1,'\n',s2,'\n',s3,'\n',s4)
print()

# When converted to a set from anyother data type, a set will return disctict data list
# omitting all repeated items. Even if you repeat an object in the collection, only one copy is retained in it
L1 =["Rohan","Physics",21,69.75]
s1 =set(L1)
T1 =(5,2,1,4,3,2,4,5)
s2 =set(T1)
string ="String will be optimized to individual set objects ommitting duplicate elements"
s3 =set(string)
print(s1,'\n',s2,'\n',s3)
print()

# Python's membership operators let you check if a certain item is available in the set. Take a look at the following example −
langs ={"C","C++","Java","Python"}
print("PHP" in langs)
print("Java" in langs)
print()

# Even if a set holds together only immutable objects, set itself is mutable.
lang1 ={"C","C++","Java","Python"}
print('Before add method: ',lang1)
lang1.add("Golang")
print('After add method: ',lang1)
print()

# update method
lang1 ={"C","C++","Java","Python"}
lang2 ={"PHP","C#","Perl"}
lang1.update(lang2)
print(lang1)
print()

# The update() method also accepts any sequence object as argument. Here, a tuple is the argument for update() method.
lang1 ={"C","C++","Java","Python"}
lang2 =("Tuple","being","updated")
lang1.update(lang2)
print(lang1)
print()

# In this example, a set is constructed from a string, and another string is used as argument for update() method.
set1 =set("Hello")
set1.update("World")
print(set1)
print()

# The union() method of set class also combines the unique items from two sets, but it returns a new set object.
lang1 ={"C","C++","Java","Python"}
print('lang1 id before union: ', id(lang1))
lang2 ={"PHP","C#","Perl"}
lang1 =lang1.union(lang2)
print ('lang1 id after uninion: ', id(lang1), (lang1))
print()

# If a sequence object is given as argument to union() method, Python automatically converts it to a set first and then performs union.
# Here a list is used as union argument. This is converted to set first and then union is performed
lang1 ={"C","C++","Java","Python"}
lang2 =["PHP","C#","Perl"]
lang3 =lang1.union(lang2)
print(lang3)
print()

# Using string as argument
set1 =set("Hello")
set2 =set1.union("World")
print(set2)
print()

# The remove() method removes the given named item from the set collection, if it is present in it. 
# However, if it is not present, it raises KeyError
lang1 ={"C","C++","Java","Python"}
print("Set before removing: ",lang1)
lang1.remove("Java")
print("Set after removing Java: ",lang1)
# Since PHP is not a named item in set, it will throw an error
# lang1.remove("PHP")
print()

'''
The discard() method in set class is similar to remove() method. 
The only difference is, it doesn't raise error even if the object to be removed is not already present in the set collection.
'''
lang1 ={"C","C++","Java","Python"}
print("Set before discarding C++: ",lang1)
lang1.discard("C++")
print("Set after discarding C++: ",lang1)
print("Set before discarding PHP: ",lang1)
lang1.discard("PHP")
print("Set after discarding PHP: ",lang1)
print()

'''
The pop() method in set class removes an arbitrary item from the set collection. 
The removed item is returned by the method. Popping from an empty set results in KeyError.
'''
lang1 ={"C","C++"}
print("Set before popping: ",lang1)
obj = lang1.pop()
print("object popped: ",obj)
print("Set after popping: ",lang1)
obj =lang1.pop()
print("object popped: ",obj)
print("Set after popping: ",lang1)
# obj =lang1.pop() # Since the set is empty after poping both items, it throws an error
print()

# The clear() method in set class removes all the items in a set object, leaving an empty set.
lang1 ={"C","C++","Java","Python"}
print(lang1)
print("After clear() method")
lang1.clear()
print(lang1)
print()

# The difference_update() method in set class updates the set by removing items that are common between itself and another set given as argument.
# Common items between s1 and s2 are removed from s1 and not s2 
s1 ={1,2,3,4,5}
s2 ={4,5,6,7,8}
print("s1 before running difference_update: ",s1)
print("s2 before running difference_update: ",s2)
s1.difference_update(s2)
print("s1 after running difference_update: ",s1)
print("s2 after running difference_update: ",s2)
print()

# As a result of intersection_update() method, the set object retains only those items which are common in itself and other set object given as argument.
# gets common items between the 2 sets and updates s1 leaving s2 as is
s1 ={1,2,3,4,5}
s2 ={4,5,6,7,8}
print("s1: ",s1,"\ns2: ",s2)
s1.intersection_update(s2)
print("a1 after intersection: ",s1)
print()

# The intersection() method in set class is similar to its intersection_update() method, 
# except that it returns a new set object that consists of items common to existing sets.
s1 ={1,2,3,4,5}
s2 ={4,5,6,7,8}
print("s1: ",s1,"\ns2: ",s2)
s3 =s1.intersection(s2)
print("s3 = s1 & s2: ",s3)
print()

'''
The symmetric difference between two sets is the collection of all the uncommon items, rejecting the common elements. 
The symmetric_difference_update() method updates a set with symmetric difference between itself and the set given as argument.
'''
s1 ={1,2,3,4,5}
s2 ={4,5,6,7,8}
print("s1: ",s1,"s2: ",s2)
s1.symmetric_difference_update(s2)
print("s1 after running symmetric difference ",s1)
print()

'''
The symmetric_difference() method in set class is similar to symmetric_difference_update() method, 
except that it returns a new set object that holds all the items from two sets minus the common items.
'''
s1 ={1,2,3,4,5}
s2 ={4,5,6,7,8}
print("s1: ",s1,"\ns2: ",s2)
s3 =s1.symmetric_difference(s2)
print("s1 = s1^s2 ",s3)
print()

# sets in loops
langs ={"C","C++","Java","Python"}
for lang in langs:
  print(lang)
print()

#using add() is loop
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("s1: ",s1,"\ns2: ",s2)
for x in s2:
	s1.add(x)
print(s1)
print()

'''
join sets using | operator
In Python, a Set is an ordered collection of items. The items may be of different types. However, an item in the set must be an immutable object. 
It means, we can only include numbers, string and tuples in a set and not lists. Python's set class has different provisions to join set objects.
The "|" symbol (pipe) is defined as the union operator. It performs the A∪B operation and returns a set of items in A, B or both. 
Set doesn't allow duplicate items.
'''
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 =s1|s2
print('s1: ', s1, '\ns2: ', s2, '\ns3: ',  s3)
print()

# The set class has union() method that performs the same operation as | operator. 
# it returns a set object that holds all items in both sets, discarding duplicates.
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3={}
print('Before union \ns1: ', s1, '\ns2: ', s2, '\ns3: ',  s3)
s3 =s1.union(s2)
print('After union \ns1: ', s1, '\ns2: ', s2, '\ns3: ',  s3)
print()

# The update() method also joins the two sets, as the union() method. 
# However it doens't return a new set object. 
# Instead, the elements of second set are added in first, duplicates not allowed.
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print('Before update \ns1: ', s1, '\ns2: ', s2)
s1.update(s2)
print('After Update \ns1: ', s1, '\ns2: ', s2)
print()

# In Python, the "*" symbol is used as unpacking operator. 
# The unpacking operator internally assign each element in a collection to a separate variable.
s1={'This', 'is', 'the', 'first', 'string'}
s2={4,5,6,7,8}
s3 ={*s1,*s2}
print('s1: ', s1, '\ns2: ', s2, '\ns3: ',  s3)
print()

# The copy() method in set class creates a shallow copy of a set object.
lang1 ={"C","C++","Java","Python"}
print("lang1: ",lang1,"id(lang1): ",id(lang1))
lang2 =lang1.copy()
print("lang2 copy of lang1: ",lang2,"id(lang2): ",id(lang2))
lang1.add("PHP")
print("After adding PHP to lang1")
print("lang1: ",lang1,"id(lang1): ",id(lang1))
print("lang2: ",lang2,"id(lang2): ",id(lang2))
print()

# Operators
# Union OPerator | (union())
s1 ={1,2,3,4,5}
s2 ={4,5,6,7,8}
s3 =s1 |s2
print('s1: ', s1, '\ns2: ', s2, '\ns1 | s2 = s3: ',  s3)
print()

# Intersection Operator & (intersectio())
s1 ={1,2,3,4,5}
s2 ={4,5,6,7,8}
s3 =s1 & s2
print('s1: ', s1, '\ns2: ', s2, '\ns1 & s2 = s3: ',  s3)
print()

# Difference Operator - (differene())
s1 ={1,2,3,4,5}
s2 ={4,5,6,7,8}
s3 =s1 - s2
print('s1: ', s1, '\ns2: ', s2, '\ns1 - s2 = s3: ',  s3)
print()

# The symmetric difference of A and B is denoted by "A Δ B" and is defined by A Δ B = (A − B) ⋃ (B − A)
# If A = {1, 2, 3, 4, 5, 6, 7, 8} and B = {1, 3, 5, 6, 7, 8, 9}, then A Δ B = {2, 4, 9}.
s1 ={1,2,3,4,5,'Raja'}
s2 ={4,5,6,7,8,'Rishi'}
print('s1: ', s1, '\ns2: ', s2)
s3 =s1 -s2
print("Difference of s1 - s2: ",s3) 
s3 =s2 -s1
print("Difference of s2 - s1: ",s3) 
s3 =s1 ^s2
print("Symmetric Difference in s1 and s2: ",s3)
print()

# Set Excercises
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
s1=set(l1)
s2=set(l2)
print('Before intersection \ns1: ', s1, '\ns2: ', s2)
commons =s1&s2 # or 
s1.intersection(s2)
commonlist =list(commons)
print('after intersection \ns1: ', s1, '\ns2: ', s2)
print('Intersected list ', commonlist)
print()

# Checking for subsets
s1={1,2,3,4,5}
s2={4,5}
if s2.issubset(s1):
	print("s2 is a subset of s1")
else:
	print("s2 is not a subset of s1")
print()

# Python program to obtain a list of unique elements in a list −
T1 =(1,9,1,6,3,4,5,1,1,2,5,6,7,8,9,2)
s1 =set(T1)
print('Original Tuple', T1)
print('Converted to set ', s1)

'''
Exercise Programs
	• Python program to find the size of a set object.
	• Python program that splits a set into two based on odd/even numbers.
	• Python program to remove all negative numbers from a set.
	• Python program to build another set with absolute value of each number in a set.
	• Python program to remove all strings from a set which has elements of different types.
'''
# Python program to find the size of a set object
T1 =(1,9,1,6,3,4,5,1,1,2,5,6,7,8,9,2)
s1 =set(T1)
print('Size of the set object ', len(s1))
print()

# Python program that splits a set into two based on odd/even numbers
T1 =(1,9,1,6,3,4,5,1,1,2,5,6,7,8,9,2)
s1 =set(T1)
sodd = s1.copy()
seven = s1.copy()
for i in s1:
	if i%2 != 0:
		seven.remove(i)
	else:
		sodd.remove(i)
print('Actual set ', s1)
print('Set of even numbers ', seven)
print('Set of odd numbers ', sodd)
print()

# Python program to remove all negative numbers from a set
T1 =(1,-9,-1,6,-3,4,-5,1,-1,-2,-5,6,7,8,9,2)
s1 =set(T1)
s2 = s1.copy()
for i in s1:
	if i < 0:
		s2.remove(i)
print('Original set', s1)
print('Removed all negetive numbers ', s2)
print()

# Python program to build another set with absolute value of each number in a set
s1 = {2.3, 4.5, 6.6, 7.2, 8.3, 9.3}
l1 = list(s1)
l2 =[]
for i in l1:
	l2.append(int(i))
print('Original set ', s1)
print('Modified set', set(l2))
print()

# Python program to remove all strings from a set which has elements of different types
s1 = {'This', 'is', 'to', 'be', 'removed', 1,2,3,'@',4+6j, 44.55, 22.45}
s2= s1.copy()
for i in s1:
	r = str(type(i))
	f = r.find('str')
	if f>0:
		s2.remove(i)
print ('Originial set ', s1)
print ('New set ', s2)
