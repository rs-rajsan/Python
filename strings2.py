'''
Following individual programs were combine into one to apply that to all examples
	• Python program to sort the characters in a string
	• Python program to remove duplicate characters from a string
	• Python program to list unique characters with their count in a string
	• Python program to find number of words in a string 
  • Python program to remove all non-alphabetic characters from a string
'''
#str = input("End a string with numbers and special characters in it :")
str = 'String object to a list. Modify the list either by INSERT(), APPEND() or REMOVE() methods'
print('Original String : \n {}'.format(str))

lst = list(str)
print(lst,'\n')

# Sorting all the characters in the string
lst.sort()
print("Sorting all characters in the string : ", lst,'\n')

# Removing Duplicates characters in the string
ulst = list(dict.fromkeys(lst))
print("Removed Duplicate values in sorted list", ulst,'\n')

# List of unique characters in the string with their count in a string
counts = {}
for char in ulst:
  counts[char] = 0
print(counts,'\n')

for cstr in str:
  if cstr in counts:
    counts[cstr]+=1

print('Every character in string and its counts as dictionary :\n')
print(counts, '\n')

# Number of words in the string
words = str.split()
print('Split the string into words \n', words)
nwords = len(words)
print('Number of words in this string is : ', nwords,'\n')

# Removing all non-alphanetic characters from the string
alst = []
for cstr in lst:
  if ord(cstr.lower()) in range(ord('a'), ord('z')):
    alst.append(cstr)

print('Removing all non-alphabetic characters from original list \n')
print(alst)
