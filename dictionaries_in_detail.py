# -------------------------------------------------------------------------
# This is a script and should not be imported as library in anyother script
# The purpose of defining main() is that to simulate C/C++/Java coding
# practice. This will help identify if the currnet script shlould be used
# standalone or can be imported in other scripts to be used as library 
#
# Since this is a standalone script, hence the definition of main()
# -------------------------------------------------------------------------

def main():
  '''
  NOTEs:
  A dictionary in Python is not a sequence, as the elements in dictionary are not indexed. 
  Still, you can use the square brackets "[ ]" operator to fetch the value associated with a certain key in the dictionary object.

  Only a number, string or tuple can be used as key. All of them are immutable. You can use an object of any type as the value.
  Python doesn't accept mutable objects such as list as key, and raises TypeError.
  '''
  d1 ={"Fruit":["Mango","Banana"],"Flower":["Rose","Lotus"]}
  d2 ={('India, USA'):'Countries',('New Delhi','New York'):'Capitals'}
  print(d1)
  print(d2)
  print()

  #   You can assign a value to more than one keys in a dictionary, but a key cannot appear more than once in a dictionary.
  d1 ={"Banana":"Fruit","Rose":"Flower","Lotus":"Flower","Mango":"Fruit"}
  d2 ={"Fruit":"Banana","Flower":"Rose","Fruit":"Mango","Flower":"Lotus"}
  print(d1)
  print(d2)
  print()

  # Using operators on dictionaries
  d1 ={'a':2,'b':4,'c':30}
  d2 ={'a1':20,'b1':40,'c1':60}
  print("Will print the value of the key 'a' ",d1['a'])
  print(d1|d2)    # Prints the union of d1 and d2
  d1|=d2      # Augments d2 to d1 and saves in d1
  print(d1)   # Prints augmented union of d1 and d2 in d1
  print()

  # Using get(), this is same as using [] (square brackets) to get the mapped value of the key
  # Unlike the "[]" operator, the get() method doesn't raise error if the key is not found; it return None.
  capitals ={"Maharashtra":"Mumbai","Gujarat":"Gandhinagar","Telangana":"Hyderabad","Karnataka":"Bengaluru"}
  print("Value of capitals['Gujarat'] is: ",capitals['Gujarat'])
  print("Value of capitals.get('Gujarat') is: ",capitals.get('Gujarat'))
  print("Value of capitals['Karnataka'] is: ",capitals['Karnataka'])
  print("Value of capitals.get('Karnataka') is: ",capitals.get('Karnataka'))

  # Key value Tamil Nadu does not exist in dictionary above
  print("Value of capitals.get('Tamil Nadu') is: ",capitals.get('Tamil Nadu'))
  
  # The get() method accepts an optional string argument. If it is given, and if the key is not found, this string becomes the return value.
  print("Capital of Haryana is : ",capitals.get('Haryana','Not found'))
  print()

  # Using dict() function without any arguments creates an empty dictionary object. It is equivalent to putting nothing between curly brackets. 
  d1 =dict()
  d2 ={}
  print('d1: ',d1)
  print('d2: ',d2)
  print()

  # Using dict() we can create a dictionary using list or tuples of two items.
  d1=dict([('a',100),('b',200)])        # List containing 2 tuples with 2 items each
  d2 =dict((('a','one'),('b','two')))   # A tuple containing 2 tuples  with 2 items each
  print('d1: ',d1)
  print('d2: ',d2)
  print()

  # The dict() function can take any number of keyword arguments with name=value pairs. 
  # It returns a dictionary object with the name as key and associates it to the value.
  d1=dict(a=100,b=200)
  d2 =dict(a='one',b='two')
  print('d1: ',d1)
  print('d2: ',d2)
  print()

  '''
  The "[]" operator (used to access value mapped to a dictionary key) is used to update an existing key-value pair as well as add a new pair.
  If the key is already present in the dictionary object, its value will be updated to val. 
  If the key is not present in the dictionary, a new key-value pair will be added.
  '''
  marks ={"Savita":67,"Imtiaz":88,"Laxman":91,"David":49}
  print("marks dictionary: ",marks)
  marks['Laxman']=95
  print("marks dictionary after update of Laxman: ",marks)
  marks['Krishan']=74
  print("marks dictionary after adding Krishnan: ",marks)
  print()

  # Updating a dictionary. Can be used in 3 ways
  # Below marks is updated with marks1. If there are keys in marks1 that does not exist in marks
  # new key:value pair is added to marks from marks1, all others are updated

  # Way No.1
  marks ={"Savita":67,"Imtiaz":88,"Laxman":91,"David":49}
  print("marks dictionary before update: ",marks)
  marks1 ={"Sharad":51,"Mushtaq":61,"Laxman":89}
  marks.update(marks1)
  print("marks dictionary after update: ",marks)
  print()

  # If the argument to update() method is a list or tuple of two item tuples, 
  # each item is added in the existing dictionary, or updated if the key is existing.
  
  # Way No.2
  marks ={"Savita":67,"Imtiaz":88,"Laxman":91,"David":49}
  print("marks dictionary before update: ",marks)
  marks1 =[("Sharad",51),("Mushtaq",61),("Laxman",89)]
  marks.update(marks1)
  print("marks dictionary after update: ",marks)
  print()

  # Third version of update() method accepts list of keyword arguments in name=value format. 
  # New k-v pairs are added, or value of existing key is updated.

  # Way No.3
  marks ={"Savita":67,"Imtiaz":88,"Laxman":91,"David":49}
  print("marks dictionary before update: ",marks)
  marks.update(Sharad =51,Mushtaq =61,Laxman =89)
  print("marks dictionary after update: ",marks)
  print()
  
  '''
  The Unpack operator
  The "**" symbol prefixed to a dictionary object unpacks it to a list of tuples, each tuple with key and value. 
  Two dict objects are unpacked and merged together and obtain a new dictionary.
  '''
  # Two dictionaries are merged and a new object is returned.
  marks ={"Savita":67,"Imtiaz":88,"Laxman":91,"David":49}
  print("marks dictionary before Unpacking: ",marks)
  marks1 ={"Sharad":51,"Mushtaq":61,"Laxman":89}
  newmarks ={**marks,**marks1}
  print("marks dictionary after Unpacking: ",newmarks)
  print()

  # Python's del keyword deletes any object from the memory. Here we use it to delete a key-value pair in a dictionary.
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  print("numbers dictionary before delete operation: ",numbers)
  del numbers[20]
  print("numbers dictionary before delete operation: ",numbers)
  print()

  # The del keyword with the dict object itself removes it from memory.
  # If tried to use that dict after deleting, will get a Variable not defined error
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  print("numbers dictionary before delete operation: ",numbers)
  del numbers
  # print("numbers dictionary before delete operation: ",numbers)
  print()

  '''
  The pop() method of dict class causes an element with the specified key to be removed from the dictionary.
  The difference between del and pop() is that del deletes the dict from memory and does not return anything and 
  The pop() method returns the value of the specified key after removing the key-value pair.
  '''
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  print("numbers dictionary before pop operation: ",numbers)
  val =numbers.pop(20)
  print("nubvers dictionary after pop operation: ",numbers)
  print("Value popped: ",val)

  # The popitem() method in dict() class doesn't take any argument. 
  # It pops out the last inserted key-value pair, and returns the same as a tuple
  # The popitem() method return a tuple contain key and value of the removed item from the dictionary
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  print("numbers dictionary before pop operation: \n",numbers)
  val =numbers.popitem()
  print("numbers dictionary after pop operation: \n",numbers)
  print("Value popped: ",val)
  print()

  # The clear() method in dict class removes all the elements from the dictionary object and returns an empty object.
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  print("numbers dictionary before clear method: ",numbers)
  numbers.clear()
  print("numbers dictionary after clear method: ",numbers)
  print()

  '''
  The items(), keys() and values() methods of dict class return view objects. 
  These views are refreshed dynamically whenever any change occurs in the contents of their source dictionary object.
  '''

  # The items() method returns a dict_items view object. It contains a list of tuples, each tuple made up of respective key, value pairs.
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  obj =numbers.items()
  print('Numbers dict items: ', numbers)
  print('type of obj: ',type(obj))
  print(obj)
  print("update numbers dictionary")
  numbers.update({50:"Fifty"})
  numbers.update({0:"Zero"})
  print("View automatically updated")
  print(obj)
  print()

  # The keys() method returns dict_keys object which is a view of keys in the dictionary.
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  obj =numbers.keys()
  print('Numbers dict items: ', numbers)
  print('type of obj: ',type(obj))
  print(obj)
  print("update numbers dictionary")
  numbers.update({50:"Fifty"})
  numbers.update({0:"Zero"})
  print("View automatically updated")
  print(obj)
  print()

  # The values() method returns a dict_values view of all the values present in the dictionary.
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  obj =numbers.values()
  print('Numbers dict items: ', numbers)
  print('type of obj: ',type(obj))
  print(obj)
  print("update numbers dictionary")
  numbers.update({50:"Fifty"})
  numbers.update({0:"Zero"})
  print("View automatically updated")
  print(obj)
  print()
  
  '''
  Unlike a list, tuple or a string, dictionary data type in Python is not a sequence, as the items do not have a positional index. 
  However, traversing a dictionary is still possible with different techniques.
  Running a simple for loop over the dictionary object traverses the keys used in it.
  '''
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  for x in numbers:
    print(x)
  print()

  # Once we are able to get the key, its associated value can be easily accessed either by using square brackets operator or with get() method.
  numbers ={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
  for x in numbers:
    print(x,":",numbers[x])
  print()
  
  # Since a variable in Python is merely a label or reference to an object in the memory, a simple assignment operator will not create copy of object.
  # When we say d1 = d2 and then update d1 with some new value, d2 is also updated
  d1 ={"a":11,"b":22,"c":33}
  d2 =d1
  print("d1 id before update:",id(d1)," d1 dict before upadte: ",d1)
  print("d2 id before update:",id(d2)," d2 dict before upadte: ",d2)
  d1["b"]=100
  print("Updating d1's b value alone to 100")
  print("d1 id after update:",id(d1)," d1 dict after upadte: ",d1)
  print("d2 id after update:",id(d2)," d2 dict after upadte: ",d2)
  print()

  # To avoid this, and make a shallow copy of a dictionary, use the copy() method instead of assignment.
  d1 ={"a":11,"b":22,"c":33}
  d2 =d1.copy()
  print("d1 id before update:",id(d1)," d1 dict before upadte: ",d1)
  print("d2 id before update:",id(d2)," d2 dict before upadte: ",d2)
  d1["b"]=100
  print("Updating d1's b value alone to 100")
  print("d1 id after update:",id(d1)," d1 dict after upadte: ",d1)
  print("d2 id after update:",id(d2)," d2 dict after upadte: ",d2)
  print()

  # Nested Dictionaries
  # A Python dictionary is said to have a nested structure if value of one or more keys is another dictionary. 
  # A nested dictionary is usually employed to store a complex data structure.
  marklist ={"Mahesh":{"Phy":60,"maths":70},"Madhavi":{"phy":75,"maths":68},"Mitchell":{"phy":67,"maths":71}}
  print(marklist)
  print()

  # Looping dictionaries
  marklist ={"Mahesh":{"Phy":60,"maths":70},"Madhavi":{"phy":75,"maths":68},"Mitchell":{"phy":67,"maths":71}}
  for k,v in marklist.items():
    print(k,":",v)
  print()
  
  # It is possible to access value from an inner dictionary with [] notation or get() method.
  print('Maths marks of Madhavi: ', marklist.get("Madhavi")['maths'])
  obj=marklist['Mahesh']
  print('Phy marks of Mahesh: ', obj.get('Phy'))
  print('Maths marks of Mitchell: ', marklist['Mitchell'].get('maths'))
  print()

  # Python program to create a new dictionary by extracting the keys from a given dictionary.
  d1 ={"one":11,"two":22,"three":33,"four":44,"five":55}
  keys =['two','five']
  d2={}
  for k in keys:
    d2[k]=d1[k]
  print(d2)
  print()

  # Python program to convert a dictionary to list of (k,v) tuples.
  d1 ={"one":11,"two":22,"three":33,"four":44,"five":55}
  L1 =list(d1.items())
  print(L1)
  print()

  # Python program to remove keys with same values in a dictionary.
  d1 ={"one":"eleven","2":2,"three":3,"11":"eleven","four":44,"two":2}
  print('Original Dictionary: ', d1)
  vals =list(d1.values()) #all values
  uvals =[v for v in vals if vals.count(v)==1] #unique values 
  print('Unique values extracted: ', uvals)
  d2 ={}
  for k,v in d1.items():
    if v in uvals:
      d ={k:v}
      d2.update(d)
  print("dict with unique value:",d2)
  print()

  '''
  Exercise Programs
	• Python program to sort list of dictionaries by values
	• Python program to extract dictionary with each key having non-numeric value from a given dictionary.
	• Python program to build a dictionary from list of two item (k,v) tuples.
	• Python program to merge two dictionary objects, using unpack operator.
  '''
  # Python program to sort list of dictionaries by values
  d1 = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
  print('Original Dictionary: ', d1)
  l1 = list(d1.values())
  print('List of dictionary values before sorting: ', l1)
  l1.sort()
  print('List of dictionary values after sorting: ', l1)
  print()

  #  Python program to extract dictionary with each key having non-numeric value from a given dictionary.
  d1 ={10:10,20:"Twenty",30:"Thirty",40:"Forty",50:'@#$%'}
  print('Original dictionary: ', d1)
  d2 = {}
  for k, v in d1.items():
    r = str(type(v))
    f = r.find('str')
    if f>0:
      d = {k:v}
      d2.update(d)
  print('new dictonary with key that has non-numeric values: ', d2)

  
if __name__ == '__main__':
  main()
