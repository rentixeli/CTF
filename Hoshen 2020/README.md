### Stage 1
```
First we'll Decode the Morse Code.
which will give us 129.213.32.20
```
### Stage 2 + 3
On the website we see a photo.

>kali@kali:~/Desktop$ binwalk Sukkah.jpg 

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
194152        0x2F668         RAR archive data, version 5.x
```



O.K there is a rar file encoded into the jpg.

>kali@kali:~/Desktop$ binwalk -E Sukkah.jpg


```
will extract us the rar. now lets bruteforce it.
kali@kali:~/Desktop/_Sukkah.jpg.extracted$ sudo rar2john 2F668.rar > text.hash
kali@kali:~/Desktop/_Sukkah.jpg.extracted$ sudo john text.hash
```



>Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
```
Password!        (2F668.rar)
1g 0:00:02:45 DONE 2/3 (2020-09-20 17:20) 0.006024g/s 570.7p/s 570.7c/s 570.7C/s Morecats2..Avalon!
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```




# Password = Password!

### Stage 4
```
After extracting the Payload.png
We can see that its a weird photo. On photoshop we will break each color to each hex code.
we will get: #666c61 #677b4d #6f6164 #696d20 #4c6573 #696d63 #68617d
which translates to ascii chars.
```
>kali@kali:~/Desktop$ echo "666c61677b4d6f6164696d204c6573696d6368617d" | xxd -r -p



>flag{Moadim Lesimcha}

