#!/usr/bin/python3
# normalize name to camel lowercase from clipboard

import pyperclip
import re

def main():
    text = pyperclip.paste()
    print("Before change:", text)
    text = str.lower(text)
    text = text.replace(' ','_')
    print("After change:", text)
    print("Already in clipboard, please paste somewhere !")
    pyperclip.copy(text)

if __name__ == "__main__":
    main()