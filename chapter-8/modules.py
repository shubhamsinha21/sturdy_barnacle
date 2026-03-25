# modules
import os
import shutil
# os.rename("chapter-8/report.txt", "chapter-8/test2.txt")
# os.remove()

# ask user for a file name and copy it
ask = input("tell me the filename: ")
shutil.copy(ask, "copy.txt")


# we use try-catch block to handle carefully file crash
try:
    file = open("chapter-8/test2.txt", "w")
    file.write("We are learning python...")
except:
    print("File is not found")