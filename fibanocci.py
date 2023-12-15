num = int(input("Enter number of digits to print in your Fibanocci series : "))
print("Printing Fibanocci Numbers to ",num," digit")
print("Printing the numbers in new line")
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

print("Done",end="\n\n")

print("Printing the numbers in Same line")
for i in range(0, (num)):
  if i == 0 : 
    prevnum = 0
    print(prevnum, ",", end = " ")
    continue
  if i == 1 : 
    currnum = 1
    print(currnum, ",", end = " ")
    continue
  if i == 2:
    nextnum = 1
    print(nextnum, ",", end = " ")
    continue
  prevnum = currnum
  currnum = nextnum
  nextnum = prevnum + currnum
  if i < num-1:
    print(nextnum, ",", end = " ")
  else:
    print(nextnum,end="\n\n")

print("Done")


