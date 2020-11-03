#!/usr/bin/env python3
from PIL import Image

im = Image.open('out copy.jpg')
pix_val = list(im.getdata())
splited = [pix_val[i::92] for i in range(92)]
h, w = 92, 304
new_im = Image.new("RGB",(w, h))
pix = new_im.load()

for y in range(h):
    line = splited[y]
    for x in range(w):
        r, g, b = line[x]
        pix[x, y] = (r, g, b)
new_im.save("out1.jpg", "JPEG")
