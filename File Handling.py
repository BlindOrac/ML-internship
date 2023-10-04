import os

"""
fh = open("filehandling.txt", "x")
fh.close()
"""

fh = open("filehandling.txt", "a")
fh.write("This is a test file for file heading part of the Python course.")
fh = open("filehandling.txt", "w")
fh.write("I opened the file on w mode to prevent the text being too long because i try my code again and again!!!")
fh = open("filehandling.txt", "r")

print(fh.read())
print(fh.readline())

if os.path.exists("filehandling.txt"):
    os.remove("filehandling.txt")
else:
    print("The file does not exist!")

# os.rmdir("myfolder")  Only empty folders can be removed
