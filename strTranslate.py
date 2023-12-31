# Use of Translate method

var ='Explicit is better than implicit.'
table =var.maketrans({'i':'I'})
print("original string:",var)
print("translation table:",table)
print()

var1 =var.translate(table)
print("Translated string",var1)
print()

var ="Explicit is better than implicit."
table =var.maketrans("than","then")
print("original string:",var)
print("translation table:",table)
print()

var2 =var.translate(table)
print("Translated string",var2)
print()

var ='Explicit is better than implicit.'
#table =var.maketrans("is","as","s")
table =var.maketrans("is","as")
print("original string:",var)
print("translation table:",table)
print()

var3=var.translate(table)
print("Translated string",var3)
