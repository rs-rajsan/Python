'''Everything about Lists here'''

# Assinings List values
list1 =["Rohan","Physics",21,69.75]
list2 =[1,2,3,4,5]
list3 =["a","b","c","d"]
list4 =[25.50,True,-55,1+2j]

print('Accessing list values using index values')
print("Item at 0th index in list1: ",list1[0])
print("Item at index 2 in list2: ",list2[2])
print()
print('Accessing list values using negetive index values')
print("Item at 0th index in list1: ",list1[-1])
print("Item at index 2 in list2: ",list2[-3])
print()
print('The slice operator extracts a sublist from the original list.')
print("Items from index 1 to 2 in list1: ",list1[1:3])
print("Items from index 0 to 1 in list2: ",list2[0:2])
print("Items from index 1 to last in list1: ",list1[1:])
print("Items from index 0 to 1 in list2: ",list2[:2])
print("Items from index 2 to last in list3",list3[2:-1])
print("Items from index 0 to index last in list4",list4[:])
print()
print('Changing list items')
print("Original list ",list3)
list3[2]=10
print("List after changing value at index 2: ",list3)
print()
print('Replace more consecutive items in a list with another sublist')
list1 =["a","b","c","d"]
print("Original list: ",list1)
list2 =['Y','Z']
list1[1:3]=list2
print("List after changing with sublist: ",list1)
print()
print('If the items are more than the list value, new values will be inserted')
list1 =["a","b","c","d"]
print("Original list: ",list1)
list2 =['X','Y','Z']
list1[1:3]=list2
print("List after changing with sublist: ",list1)
print()
print('If the replacing list is smaller than the slice, remaining item in original list is removed')
list1 =["a","b","c","d"]
print("Original list: ",list1)
list2 =['Z']
list1[1:3]=list2
print("List after changing with sublist: ",list1)
print()
print('Appending an item to list')
list1 =["a","b","c","d"]
print("Original list: ",list1)
list1.append('e')
print("List after appending: ",list1)
print()
print('Inerting into a list')
list1 =["Rohan","Physics",21,69.75]
print("Original list ",list1)
list1.insert(2,'Chemistry')
print("List after appending: ",list1)
list1.insert(-1,'Pass')
print("List after appending: ",list1)
print('''We know that "-1" index points to the last item in the list. However, note that, the item at index "-1" in the original list is 69.75. 
This index is not refreshed after appending 'chemistry'. Hence, 'Pass' is not inserted at the updated index "-1", but the previous index "-1".''')
print()
print('Removing items from list. Removes the first occurance of the specified item')
list1 =["Rohan","Physics",21,69.75]
print("Original list: ",list1)
list1.remove("Physics")
print("List after removing: ",list1)
print()
print('pop() method to remove list items. Removes items based on specified index')
list2 =[25.50,True,-55,1+2j]
print("Original list: ",list2)
list2.pop(2)
print("List after popping: ",list2)
print()
print(' "del" keyword that deletes any Python object from the memory')
list1 =["a","b","c","d"]
print("Original list: ",list1)
del list1[2]
print("List after deleting: ",list1)
list2 =[25.50,True,-55,1+2j]
print("List before deleting: ",list2)
del list2[0:2]
print("List after deleting: ",list2)




