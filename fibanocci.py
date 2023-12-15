num = int(input("Enter number of digits to print in your Fibanocci series : "))
print("Printing Fibanocci Numbers to ",num," digit")

for i in range(0, (num)):
  if i == 0 : 
    prevnum = 0
    print("Digit ",i+1,". ",prevnum)
    continue
  if i == 1 : 
    currnum = 1
    print("Digit ",i+1,". ",currnum)
    continue
  if i == 2:
    nextnum = 1
    print("Digit ",i+1,". ",nextnum)
    continue
  prevnum = currnum
  currnum = nextnum
  nextnum = prevnum + currnum
  print("Digit ",i+1,". ",nextnum)

print("Done")


