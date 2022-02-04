import os

path = "C:\\Users\\Family\\OneDrive\\Desktop\\test"

if os.path.exists(path):
    print("That location exists! ")
    if os.path.isfile(path):
        print("That is a file")
    else:
        print("That is a directory")
else:
    print("That location doesn't exist!")
