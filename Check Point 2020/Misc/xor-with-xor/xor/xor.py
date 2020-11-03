def xor(data, key):
	return bytearray(((data[i] ^ key[i % len(key)]) for i in range(0, len(data))))

data = bytearray(open('xor-with-xor.bin', 'rb').read())
key = bytearray([0x78, 0x6F, 0x72])
msg = xor(data,key)
f = open('test.zip', 'wb')
f.write(msg)
f.close()
