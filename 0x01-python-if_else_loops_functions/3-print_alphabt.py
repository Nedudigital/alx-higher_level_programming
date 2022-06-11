#!/usr/bin/python3
# Author - Chinedu Ndubisi
for letter in range(100, 126):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
