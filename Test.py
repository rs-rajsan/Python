s1 = {'This', 'is', 'to', 'be', 'removed', 1,2,3,'@',4+6j, 44.55, 22.45}
s2= s1.copy()
for i in s1:
	r = str(type(i))
	f = r.find('str')
	if f>0:
		s2.remove(i)
print ('Originial set ', s1)
print ('New set ', s2)
