```
after examining the files we can see 2 suspicious packets. start & end.
after setting 'udp.port == 22' which was their port. we will get some packets between those start and end. I tried to examine the packets but after a while i saw something strange. they all start in 5XXX in the info section. that seemed to me like a dec chars on ascii table. so i built a script that give me the chars of those dec and got the flag.
112, 105, 99, 111, 67, 84, 70, 123, 112, 49, 76, 76, 102, 51, 114, 51, 100, 95, 100, 97, 116, 97, 95, 118, 49, 97, 95, 115, 116, 51, 103, 48, 125
```

## picoCTF{p1LLf3r3d_data_v1a_st3g0}
