#!/usr/bin/env python3
count = 0
c = 0
with open('aap.txt', 'r') as file:
	lines = file.readlines()
	for line in lines:
		for num in range(98):
			#left to right
			if line[num] == '1' and line[num+1] == '2' and line[num+2] == '3':
				count += 1
			#right to left
			if line[num] == '3' and line[num+1] == '2' and line[num+2] == '1':
				count += 1
	for num in range(100):
		for i in range(98):
			#up to down
			if lines[i][num] == '1' and lines[i+1][num] == '2' and lines[i+2][num] == '3':
				count += 1
			#down to up
			if lines[i][num] == '3' and lines[i+1][num] == '2' and lines[i+2][num] == '1':
				count += 1
	for num in range(98):
		for i in range(98):
			#alachson left2right up2down
			if lines[i][num] == '1' and lines[i+1][num+1] == '2' and lines[i+2][num+2] == '3':
				count += 1
			#alachson right2left down2up
			if lines[i][num] == '3' and lines[i+1][num+1] == '2' and lines[i+2][num+2] == '1':
				count += 1
	for num in range(99, -1, -1):
		for i in range(98):
			#alachson right2left up2down
			if lines[i][num] == '1' and lines[i+1][num-1] == '2' and lines[i+2][num-2] == '3':
				count += 1
			#alachson left2right down2up
			if lines[i][num] == '3' and lines[i+1][num-1] == '2' and lines[i+2][num-2] == '1':
				count +=1
print (count)
