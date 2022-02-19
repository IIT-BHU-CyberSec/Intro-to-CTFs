## Solutions:

### strings_demo.jpg
Run this command in a terminal inside the directory containing ```strings_demo.jpg```  
(The last line of the output will be the flag)  
```console
strings strings_demo.jpg
```   
Alternatively, you can open the file in a text editor (like notepad) and the last line will contain the flag.  

### exiftool_demo.jpg
Run this command in a terminal inside the directory containing ```exiftool_demo.jpg```  
(The flag will be in the line containing "Comment")  
```console
exiftool exiftool_demo.jpg
```
### binwalk_demo.jpg
Run this command in a terminal inside the directory containing ```binwalk_demo.jpg```   
(This command will list all embedded files inside the specified file and extract these files to a new directory named ```_binwalk_demo.jpg.extracted```)
```console
binwalk -D=".*" binwalk_demo.jpg
```
Open these extracted files with an image viewer and the second image will contain the flag
