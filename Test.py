d1 ={10:10,20:"Twenty",30:"Thirty",40:"Forty",50:'@#$%'}
print('Original dictionary: ', d1)
d2 = {}
for k, v in d1.items():
	r = str(type(v))
	f = r.find('str')
	if f>0:
		d = {k:v}
		d2.update(d)
print('new dictonary with key that has non-numeric values: ', d2)
