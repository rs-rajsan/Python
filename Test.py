def testfunction(arg):
	print("Inside function:",arg)
	print("ID inside the function:",id(arg))
	arg=arg.append(100)

var=[10,20,30,40]
print("ID before passing:",id(var))
testfunction(var)
print("list after function call",var)
