def xor(data, key):
	return bytearray(((data[i] ^ key[i % len(key)]) for i in range(0, len(data))))

data = bytearray(open('secretzz.png', 'rb').read())
key = bytearray([0x6e, 0x30, 0x30, 0x62, 0x3d, 0x3d])
msg = xor(data,key)
f = open('test', 'wb')
f.write(msg)
f.close()
