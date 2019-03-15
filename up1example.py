#!/usr/bin/python3
# move the example*.py up 1 level and take name of father directory
# chose the directory to run, not all directory *
# if there is another file than example*.py, copy to father directory
# note: before move and delete, print the message to confirm
# note: only run only one times, be carefully if run the second time

import os
import shutil
import re

fileRegex = re.compile(r'''
    ^               # start with..
    example         # file name example
    (.*?)
    \.py            # extension: .py
    $               # end file name
    ''', re.VERBOSE)

target_dir = "./1"
os.chdir(target_dir)
abs_dir = os.path.abspath(os.getcwd())

newfiles = []
oldfiles = []

def main():
    print("Current working directory", abs_dir)
    for dir_ in os.listdir():
        if os.path.isdir(dir_):
            for file in os.listdir(dir_):
                # neu file la example*.py thi move va doi ten, con khong thi move vao thu muc cha
                # chi xet 1 cap thu muc thoi
                oldfiles.append(os.path.join(abs_dir, dir_, file))
                if fileRegex.match(file):
                    newfile = os.path.join(abs_dir, fileRegex.sub(r'%s\1.py' % dir_ , file))
                else:
                    newfile = os.path.join(abs_dir, file)
                newfiles.append(newfile)
        # xoa thu muc empty
            # if len(os.listdir(dir_)) == 0:
            #     shutil.rmtree(os.path.join(abs_dir, dir_))


    print("Files will be move:")
    for old, new in zip(oldfiles, newfiles):
        # print(old)
        # print("--->", new)
        # print("-"*40)
        shutil.move(old, new)


if __name__ == "__main__":
    main()