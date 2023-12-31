#String formatting using Template class
from string import Template
temp_str ="My name is $name and I am $age years old"
tempobj =Template(temp_str)
ret =tempobj.substitute(name='Rajesh',age=23)
print(ret)

#We can also unpack the key-value pairs from a dictionary to substitute the values.

student ={'name':'Rajesh','age':23}
temp_str ="My name is $name and I am $age years old"
tempobj =Template(temp_str)
ret =tempobj.substitute(**student)
print(ret)
