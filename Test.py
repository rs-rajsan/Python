tstr = ('Python', 'program', 'to', 'sort', 'a', 'tuple', 'of', 'strings', 'on', 'the', 'number', 'of', 'alphabets', 'in', 'each', 'word')
print('Original Tuple: ', tstr)
lstr = list(tstr)

for i in range(0,len(lstr)-2):
  for j in range(i,len(lstr)):
    if (len(lstr[j])) <= (len(lstr[i])):
      str1 = lstr[i]
      str2 = lstr[j]
      lstr.pop(i)
      lstr.insert(i, str2)
      lstr.pop(j)
      lstr.insert(j, str1)
'''
if (len(lstr[0])) <= (len(lstr[1])):
  str1 = lstr[0]
  str2 = lstr[1]
  print('Before Pop: ',lstr)
  lstr.pop(0)
  lstr.insert(0, str2)
  lstr.pop(1)
  lstr.insert(1, str1)
  print('After Pop: ', lstr)

'''
      
tstr = tuple(lstr)
print('Sorted Tuple: ', tstr)
