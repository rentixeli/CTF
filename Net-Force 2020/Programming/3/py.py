#!/usr/bin/env python3
from decimal import *
getcontext().prec = 5003
x = Decimal(13155187) / Decimal(13417)
y = str(x)
z = len(y)
print (y[z-6:z])
