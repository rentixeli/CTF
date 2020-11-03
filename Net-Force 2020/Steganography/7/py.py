l = '2C7CBi*66iC6C2BBB3i6B36i<;][XJ\D>AQJ>Q7[\C;|Q[M]>917,.E.|G]B>S.2X3YXYXXY./YY.2Y3XY32.X.Yl//lmml.63mm2*l6.+7lml622336*26/'
z = ''
k = ''
po = 0
for char in l:
	z = bin(ord(char))
	po = len(z)
	k = k + z[po - 1]

#print (k)


m = ''
j = ''
for x in k:
	if len(j) < 8:
		j = j + x
	else:
		m = m + ' ' + j
		j = x
print (m + ' ' + j)
