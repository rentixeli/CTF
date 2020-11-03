#!/usr/bin/env python3

k = ''
b = ''
with open('whitepages.txt', 'r') as file:
	z = file.readlines()
	k = z
	for i in k:
		for a in i:
			if a == ' ':
				b = b + '1'
			else:
				b = b + '0'

k = ''
m = ''

for e in b:
	if len(k) < 8:
		k = k + e
	elif len(k) == 8:
		m = m + k + ' '
		k = e
print (m + k)
