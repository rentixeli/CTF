#!/usr/bin/env python3
import requests
url =  'https://www.net-force.nl/challenge/level602/prog2.php'
page = requests.get(url)
z = '0123456789'
lo = ''
x = page.content
y = str(x)
for c in y:
	for k in z:
		if c == k:
			lo = lo + k
print ((int(lo[:-6]) * 3 + 2) - 250)
kok = str(int(lo[:-6]) * 3 + 2 - 250)
jon = url + '?solution=' + kok
page2 = requests.get(jon)
print (str(page2.content))
