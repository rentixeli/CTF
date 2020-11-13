Challenge:
```
"One day, after getting tired of being made fun of by all the other hackers, he decided to finally take a look at BASH.
His first thoughts were 'Bash? Bash Windows? Oh those violent script kiddies!'. After finishing hundreds of online tutorials,
he accidentally (obviously)found a flag. His next status update was ' The script kiddies will never be able to get the flag from this password protected binary.
How dare he call you and us 'script kiddies'?! Take him down.

Here is the file . For 32bit users - file
The flag is SHA-256 of the MD-5 hash obtained."
```

We will use hexeditor to view the raw text of the file.
![picture](https://i.ibb.co/FKCfDNt/Untitled.png)

Bingo! Now all we got to do is to test each password.
```
kali@kali:~/Downloads$ ./binaary50 Masternamer
3cd50c6be9bbede06e51741928d88b7e
sha256
```

Now we need to encode it using sha256 and we'll have our flag.
## dad827e94c609b76424287f2523b2117475df29e4ca8475444a9976faedc00f7
