'''Example 1
Python program to find number of vowels in a given string.'''

mystr ="All animals are equal. Some are more equal"
vowels ="aeiou"
count=0
for x in mystr:
  if x.lower() in vowels:
    count+=1

print("Number of Vowels:",count)

''' Example 2
Python program to convert a string with binary digits to integer.'''

mystr ='10101'

def strtoint(mystr):
	for x in mystr:
		if x not in'01':
			return "Error. String with non-binary characters"
		num =int(mystr,2)
		return num

print("binary:{} integer: {}".format(mystr,strtoint(mystr)))

''' Example 3
Python program to drop all digits from a string.'''

# Creating a list of digits from 1 to 9 as individual strings
digits =[str(x) for x in range(10)]
mystr ='He12llo, Py00th55on!'
chars =[]
for x in mystr:
	if x not in digits:
		chars.append(x)
		
    #Converting list to a String
		newstr =''.join(chars) 

print(digits)
print(newstr)
