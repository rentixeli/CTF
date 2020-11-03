import sys
def f1(s1,s2):
    return ''.join(chr(ord(x1) ^ ord(x2)) for x1,x2 in zip(s1,s2))
def f2(s, x):
    return (s*(int(x/len(s))+x))[:x]
key = sys.argv[1]
flag = sys.argv[2]
for c in key:
	if not c.isalnum():
		sys.exit()
e = f1(flag, f2(key, len(flag)))
with open('encrypted', 'w') as fh:
	fh.write(e.encode().hex())
