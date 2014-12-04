instagram-image-dumper
======================

A Github Repo for Instagram image dumper scripts
No license for the instagram-image-dumper.ps1 and instagram-image-dumper.py! Do what ever you want with it!

instagram-image-dumper.sh is licensed under GPL

instagram-image-dumper.ps1
--------------------------
PowerShell Script works only with version 3!

You just need to set the username of the Instagram user and the local download path for the images.

instagram-image-dumper.py
--------------------------
Python version of the script

```
root@example.org:~/Sources/instagram-image-dumper# ./instagram-image-dumper.py -h
usage: instagram-image-dumper.py [-h] [-d DOWNLOADPATH] -u USERNAME

optional arguments:
  -h, --help            show this help message and exit
  -d DOWNLOADPATH, --downloadpath DOWNLOADPATH
                        The path you wish to download all images.
  -u USERNAME, --username USERNAME
                        The name of the user whose images you want to download
```

instagram-image-dumper.sh
--------------------------
Bash version of the script

```
root@example.org:~# bash instagram-image-dumper.sh instaname
```
