Challenge:
```
My TV was broadcasting something about sin3point14 when h4ck3y3 came in with his pesky XOR tricks
http://static.beast.sdslabs.co/static/noob/secretzz.png
```
From the challenge name we understand that the bytes of the file has been changed using xor.

I used an online website to check what xor key they possibly used and I've got: n00b==

which on hex is: 6e 30 30 62 3d 3d

I wrote a script that xor the bits with the key.
```def xor(data, key):
	return bytearray(((data[i] ^ key[i % len(key)]) for i in range(0, len(data))))

data = bytearray(open('secretzz.png', 'rb').read())
key = bytearray([0x6e, 0x30, 0x30, 0x62, 0x3d, 0x3d])
msg = xor(data,key)
f = open('test', 'wb')
f.write(msg)
f.close()
```
![1](https://i.ibb.co/bQ7v0tT/test.png)
>flag{sin3point14_w4tch35_b0ku_n0_pic0}
## sha256: f54e88f505d5d1f10c1196af96eef0a506af816ee1e5a12893acb7dbc7b1c5f3
