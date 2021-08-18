import base64
def xor(data, key):
    l = len(key)
    return bytearray((
        (data[i] ^ key[i % l]) for i in range(0,len(data))
    ))
with open ('keys', 'rb') as keyz:
	string = keyz.read()
	key = bytearray([0xCC,0x55,0xAA])
	print(xor(string, key).decode())
