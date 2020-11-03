#!/usr/bin/env python3
import requests
x = int(str(requests.get('https://www.net-force.nl/challenge/level602/prog2.php').content)[32:37])
print (str(requests.get('https://www.net-force.nl/challenge/level602/prog2.php?solution=' + str(x * 3 + 2 - 250)).content))
