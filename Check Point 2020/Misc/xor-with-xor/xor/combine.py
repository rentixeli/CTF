f = open('combined.gz', 'wb')
for i in range(1000):
	data = bytearray(open(str(i) + '.dat', 'rb').read())
	f.write(data)
f.close()
