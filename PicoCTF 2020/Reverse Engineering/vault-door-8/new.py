#!/usr/bin/env python3
import binascii
#23670145 -> 0-11V
a = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xE0, 0x95, 0xF1, 0xE1, 0xE0, 0xA4, 0xC0, 0x94, 0xA4]
ans = ''
answer = ''
for i in a:
	x = bin(i)
	x = x[2:]
	if len(x) == 8:
		ans = ''.join(x[4]+x[5]+x[0]+x[1]+x[6]+x[7]+x[2]+x[3])
		answer = answer + chr(int(ans,2))
	elif len(x) == 7:
		x = '0' + x
		x = str(x)
		ans = ''.join(x[4]+x[5]+x[0]+x[1]+x[6]+x[7]+x[2]+x[3])
		answer = answer + chr(int(ans,2))
	elif len(x) == 6:
		x = '00' + x
		x = str(x)
		ans = ''.join(x[4]+x[5]+x[0]+x[1]+x[6]+x[7]+x[2]+x[3])
		answer = answer + chr(int(ans,2))
print (answer)
