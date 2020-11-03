#!/usr/bin/env python3
a = '415F6231745F30665F6231745F7368316654694E675F64633830653238313234'
b = ''
x = -1
for i in range(0, 63, 2):
	x += 1
	b= b + a[i] + a[i+1] + ''

print (bytes.fromhex(b).decode('utf-8'))
