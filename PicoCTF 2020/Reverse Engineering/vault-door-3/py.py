#!/usr/bin/env python3
a = 'jU5t_a_sna_3lpm18g947_u_4_m9r54f'
index = 0
k = list(a)
for i in range(0, 8):
	k[i] = a[i]
for i in range(8, 16):
	k[i] = a[23-i]
for i in range(16, 32, 2):
	k[i] = a[46-i]
for i in range(31, 17, -2):
	k[i] = a[i]
print (k)

#visible string
l = ''
for i in k:
	l = l + ''.join(i)
print (l)
