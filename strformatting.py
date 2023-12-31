''' All examples of using % as formatting method similar to C language'''
print("My name is %s and weight is %d kg!"%('Zara',21))

name="Rajesh"
age=23
print("my name is %s and my age is %d years"%(name,age))

#Space padding to the left
a=1
b=11
c=111
print("a=%5d b=%5d c=%5d"%(a,b,c))

# Printing decimals
name="Rajesh"
age=23
percent=55.50
print("my name is %s, age %d and I have scored %6.3f percent marks"%(name,age,percent))

# Left padding spaces to a string
name='TutorialsPoint'
print('Welcome To %20s The largest Tutorials Library'%(name,))
print('Welcome To %-20s The largest Tutorials Library'%(name,))

#Add a '. ' to the format to truncate longer string.
#Creates a substring of the actual string
name='TutorialsPoint'
print('Welcome To %.5s The largest Tutorials Library'%(name,))

''' Using format() method. introduced in Python 3.0, also have been
backported to 2.6 & 2.7'''

#The print statement contains placeholders {} in which values of variables are successively inserted
name="Rajesh"
age=23
print("\nUsing format(): \n\nmy name is {} and my age is {} years".format(name,age))
print ("my name is {name} and my age is {age} years".format(name="Raja", age=25))

'''
You can also specify C style formatting symbols. Only change is using ":" instead of %.
For example, instead of %s use {:s} and instead of %d use (:d}
'''
name="Rishi"
age=18
print("my name is {:s} and my age is {:d} years".format(name,age))

name="Rajesh"
age=23
percent=55.50
print("my name is {:s}, age {:d} and I have scored {:6.3f} percent marks".format(name,age,percent))
print('\n')
'''
String alignment is done with <, > and ^ symbols (for left, right and center alignment respectively) in place holder. 
Default is left alignment.
'''
name='TutorialsPoint'
print('Welcome To {:>20} The largest Tutorials Library'.format(name))
print('Welcome To {:<20} The largest Tutorials Library'.format(name))
print('Welcome To {:^20} The largest Tutorials Library'.format(name))

#Similarly, to truncate the string use a "." in the place holder.
name='TutorialsPoint'
print ('Welcome To {:.5} The largest Tutorials Library'.format(name))

#Using f-String formatting
# Python f-strings are a faster, more readable, more concise, and less error prone.
print('\n')

name ='Rajesh'
age =23
fstring =f'My name is {name} and I am {age} years old'
print(fstring)

# The f-string may contain expressions inside the {} placeholder.
price =10
quantity =3
fstring =f'Price: {price} Quantity : {quantity} Total : {price*quantity}'
print(fstring)

# The placeholders can be populated by dictionary values.
user ={'name':'Ramesh','age':23}
fstring =f"My name is {user['name']} and I am {user['age']} years old"
print(fstring)

# The = character is used for self debugging the expression in f-string.
price =10
quantity =3
fstring =f"Total : {price*quantity=}"
print(fstring)

#Printing floats
name="Rajesh"
age=23
percent=55.50
fstring =f"My name is {name} and I am {age} years old and I have scored {percent:6.3f} percent marks"
print(fstring)

#Alignments
name='TutorialsPoint'
fstring =f'Welcome To {name:>20} The largest Tutorials Library'
print(fstring)
fstring =f'Welcome To {name:<20} The largest Tutorials Library'
print(fstring)
fstring =f'Welcome To {name:^20} The largest Tutorials Library'
print(fstring)

#The f-strings can display numbers with hexadecimal, octal and scientific notation
num=20
fstring =f'Hexadecimal : {num:x}'
print(fstring)
fstring =f'Octal :{num:o}'
print(fstring)
fstring =f'Scientific notation : {num:e}'
print(fstring)
