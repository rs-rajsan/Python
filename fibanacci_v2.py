# Adding fibanocci series in a list and printing the list
lst = [0,1,1]
# print(lst)
num = int(input("Enter number of Digits to print in your Fibanocci Series : "))

# Starting for loop to append next value in series
for i in range(3, num):
  # Appending items to list
  lst.append(lst[i-2]+lst[i-1])

# Printing the Series
print(lst)
#print(globals())
