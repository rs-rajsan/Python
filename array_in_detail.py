import array as arr
import copy  as cpy

def main():

  # creating an array with integer type 

  a =arr.array('i',[1,2,3])
  print(type(a),a) 

  # creating an array with char type
  a =arr.array('u','BAT')
  print(type(a),a)

  # creating an array with float type 
  a =arr.array('d',[1.1,2.2,3.3])
  print(type(a),a)
  print()

  # Since the array object behaves very much like a sequence, you can perform indexing and slicing operation with it.
  # Indexing starts with 0 as in C/C++
  a =arr.array('i',[1,2,3])
  print('Original array: ', a)
  #indexing
  print('a[1] : ',a[1])
  #slicing
  print('a[1:] : ', a[1:])
  print()

  # Multiple ways to add items to array
  # append() method
  a =arr.array('i',[1,2,3])
  print('Original array: ', a)
  a.append(10)
  print('Appended new value in the end: ', a)
  print()

  # insert() method
  a =arr.array('i',[1,2,3])
  print('Original array: ', a)
  a.insert(1,70)
  print('Inserted new value in index 1: ', a)
  print()

  # extend() method
  a =arr.array('i',[1,2,3,4,5])
  b =arr.array('i',[6,7,8,9,10])
  print('Original array a: ', a)
  print('Original array b: ', b)
  a.extend(b)
  print('a extednded with b: ', a)
  print()

  # There are 2 methods to remove an array element from an array
  # The remove() method removes the first occurrence of a given value from the array
  a =arr.array('i',[1,2,1,4,2])
  print('Original array a: ', a)
  a.remove(2)
  print('After removing 1st occurance of element 2: ',a)
  print()

  # The pop() method removes an element at the specified index from the array, and returns the removed element.
  a =arr.array('i',[1,2,3,4,2])
  print('Original array a: ', a)
  b = a.pop(2)
  print('a.pop(2) : 2 is the index of the poped element: ', b)
  print('After poping the element 2: ', a)
  print()

  # Looping arrays
  # for loop type 1
  a =arr.array('d',[1,2,3])
  print('regular for loop: ', a)
  for x in a:
    print(x)
  print()

  # for loop type 2
  a =arr.array('d',[1,2,3])
  l =len(a)
  print('for loop with length of array: ', a)
  for x in range(l):
    print(a[x])
  print()

  # while loop
  a =arr.array('d',[1,2,3])
  l =len(a)
  print('while loop: ', a)
  idx =0
  while idx<l:
    print(a[idx])
    idx+=1
  print()

  # copy an array. Assignment doesn't create a new array in the memory
  # a and b refer to same memory location, meaning same array
  a =arr.array('i',[1,2,3,4,5])
  b=a
  print('Memory id of a: ', id(a), ' for array a: ', a)
  print('Memory id of b: ', id(b), ' for array b: ', b)
  print()
  # Because "a" and "b" refer to the same array object, any change in "a" will reflect in "b" too
  a[2]=10
  print('array a after update of a: ', a)
  print('array b after update of a: ', b)
  print()

  '''
  To create another physical copy of an array, we use another module in Python library, named copy and use deepcopy() function in the module. 
  A deep copy constructs a new compound object and then, recursively inserts copies into it of the objects found in the original.
  You will have to import copy module to do deep copy
  '''
  a =arr.array('i',[1,2,3,4,5])
  b=cpy.deepcopy(a)
  print('Memory id of a: ', id(a), ' for array a: ', a)
  print('Memory id of b: ', id(b), ' for array b: ', b)
  print()
  # Updating a alone. This does not change anything in b as b a new physical copy of a
  a[2]=10
  print('array a after update of a: ', a)
  print('array b after update of a: ', b)
  print()

  # rearranging arrays in reverse order of the index
  a =arr.array('i',[10,5,15,4,6,20,9])
  
  # declaring an empty array
  b =arr.array('i')
  
  # Here we loop array a to its length from last item to first and append each item to b
  for i in range(len(a)-1,-1,-1):
    b.append(a[i])
  print('array a: ', a)
  print('array b: ', b)
  print()

  # We can also reverse the sequence of numbers in an array using the reverse() method in list class.
  # We have to first transfer the contents of an array to a list with tolist() method of array class
  a =arr.array('i',[10,5,15,4,6,20,9])
  print('Original array a: ',a)
  b =a.tolist()       # converting array a to list and assigning it to b
  print('array a as list in b', b)
  b.reverse()         # using the reverse()
  print('list b in reverse order using reverse() method: ', b)
  c =arr.array('i')   # declaring empty array
  c.fromlist(b)       # converting the list b to array and assigning to c
  print('converting list b to array and assingin it to c', c)
  print()

  # The array class doesn't have any function/method to give a sorted arrangement of its elements.

  # Using a sorting algorithm (bubble sort)
  a =arr.array('i',[10,5,15,4,6,20,9])
  print('Original array a: ', a)
  for i in range(0,len(a)):
    for j in range(i+1,len(a)):
      if(a[i]>a[j]):
        temp =a[i];
        a[i]=a[j];
        a[j]=temp;
  print('Sorted array a:', a)
  print()

  # Using the sort() Method from List
  a =arr.array('i',[10,5,15,4,6,20,9])
  print('Original array a: ',a)
  b =a.tolist()       # converting array a to list and assigning it to b
  print('array a as list in b', b)
  b.sort()         # sort() method of list used to sort the list b
  print('sort() method of list used to sort the list b: ', b)
  c =arr.array('i')   # declaring empty array
  c.fromlist(b)       # converting the list b to array and assigning to c
  print('converting list b to array and assingin it to c', c)
  print()

  # Using the Builtin sorted() Function
  # The sorted() function can be used along with any iterable. Python array is an iterable as it is an indexed collection. 
  # Hence, an array can be used as a parameter to sorted() function.
  # The function returns a new list containing all items from the iterable in ascending order. 
  # Set reverse parameter to True to get a descending order of items.
  a =arr.array('i',[4,5,6,9,10,15,20])
  print('Original array a: ',a)
  sorted(a)
  print('array a after using sorted() method: ',a)
  print()

  # Join Arrays
  # Using append() method
  a =arr.array('i',[10,5,15,4,6,20,9])
  print('Original array a: ',a)
  b =arr.array('i',[2,7,8,11,3,10])
  print('Original array b: ',b)
  c = cpy.deepcopy(a)              # copying a to c
  print('copy of array a to c: ',c)
  for i in range(len(b)):
    c.append(b[i])
  print('Joined array c: ', c)
  print()

  # Converting arrays to list and using list operations to add
  a =arr.array('i',[10,5,15,4,6,20,9])
  print('Original array a: ',a)
  b =arr.array('i',[2,7,8,11,3,10])
  print('Original array b: ',b)
  x=a.tolist()        # Converting array a to list x
  y=b.tolist()        # Converting array b to list y
  z=x+y               # adding x and y and save it at z
  c=arr.array('i')    # initializing c
  c.fromlist(z)       # Converting list z to array in c
  print('Added array a and b in c: ', c)
  print()

  # Using extend() class
  a =arr.array('i',[10,5,15,4,6,20,9])
  print('Original array a: ',a)
  b =arr.array('i',[2,7,8,11,3,10])
  print('Original array b: ',b)
  c=arr.array('i')    # initializing c
  c.extend(b)
  print('b is extended to a and saved in c: ', c)
  print()

  '''
  Exercise Programs
	• Python program find difference between each number in the array and the average of all numbers
	• Python program to convert a string in an array
	• Python program to split an array in two and store even numbers in one array and odd numbers in the other.
	• Python program to perform insertion sort on an array.
	• Python program to store the Unicode value of each character in the given array.
  '''

  # Python program find difference between each number in the array and the average of all numbers
  a =arr.array('i',[10,5,15,4,6,20,9])
  d = arr.array('i')
  for i in range(len(a)-1):
    d.append(a[i]-a[i+1])
  avg = sum(a)/len(a)
  print('Original Array a: ', a)
  print('differnce of each element of array a: ', d)
  print('Avg of all elements of array a: ', avg)
  print()
  
  # Python program to convert a string in an array
  str = 'This is the string that needs to be converted into an array'
  sa = str.split(' ')
  sl = list(str)
  print('As a String: ', str)
  print('Arrany of strings as a list: ', sa)
  print('Arrany of chars as a list: ', sl)
  print()

  # Python program to split an array in two and store even numbers in one array and odd numbers in the other
  a =arr.array('i',[10,5,15,4,6,20,9])
  e = arr.array('i')
  o = arr.array('i')
  for i in range(len(a)):
    if a[i]%2==0:
      e.append(a[i])
    else:
      o.append(a[i])
  print('Original Array of numbers a:', a)
  print('Seperated even numbers e: ', e)
  print('Seperated odd numbers o: ', o)
  print()

  # Python program to perform insertion sort on an array
  a = arr.array('i',[12, 11, 13, 5, 6])
  print('array a before insertion sort: ', a)
  for i in range(1, len(a)):  # Iterate over the array starting from the second element
    key = a[i]  # Store the current element as the key to be inserted in the right position
    j = i-1
    while j >= 0 and key < a[j]:  # Move elements greater than key one position ahead
        a[j+1] = a[j]  # Shift elements to the right
        j -= 1
    a[j+1] = key  # Insert the key in the correct position
  print('array a after insertion sort: ', a)

  # Uncomment  the below code to understand the logic of the insertion sort
  '''
    a = arr.array('i',[12, 11, 13, 5, 6])
  for i in range(1, len(a)):
    ic('index = ',i,' and its value ', a[i])

  print('array a before insertion sort: ', a)
  for i in range(1, len(a)):  # Iterate over the array starting from the second element
    key = a[i]  # Store the current element as the key to be inserted in the right position
    j = i-1
    ic(key, i, j)
    while j >= 0 and key < a[j]:  # Move elements greater than key one position ahead
        a[j+1] = a[j]  # Shift elements to the right
        ic('Before j-1',j, a[j+1], a[j])
        j -= 1
        ic('after j-1',j, a[j+1], a[j])
    a[j+1] = key  # Insert the key in the correct position
    ic('assinging key to j+1', a[j+1], key)
  print('array a after insertion sort: ', a)

  '''
  # Python program to store the Unicode value of each character in the given array

if __name__ == '__main__':
  main()
