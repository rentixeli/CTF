#!/usr/bin/env python3
x = 1
y = 1
prev = 1
ans = x * y + prev + 3

while x != 525:
	x += 1
	y += 1
	prev = ans
	ans = x * y + prev + 3
print (ans)
