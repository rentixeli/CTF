```
on this one we need to fix the headers of the doc. (or just use binwalk)
after fixing the headers of the file we get a picture.
after using zsteg i saw this: 'b1,rgb,lsb,xy       .. text: "48:UTFOQmUxTjBNemxoVGpCZklXNWZaREJqWHpGelgwNHhZek45"'
'UTFOQmUxTjBNemxoVGpCZklXNWZaREJqWHpGelgwNHhZek45'
It seemed to me like a base64.. so i decoded it and got 'Q1NBe1N0MzlhTjBfIW5fZDBjXzFzX04xYzN9'
I thought to myself maybe I did something wrong or missed something but then I thought to decode it again with base64 and got the flag. :)
```
## CSA{St39aN0_!n_d0c_1s_N1c3}
