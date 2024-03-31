# https://www.w3schools.com/python/module_os.asp ,also https://docs.python.org/3/library/os.html
# https://www.youtube.com/watch?v=dkVYSsL90Oo
import os

try:   # always better to check file/folder exists in order to avoid error
    os.mkdir("resources/OSmod") # making a folder
except FileExistsError:
    print(f"File already exists")
try:
    for i in range(1, 10):
        os.mkdir(f"resources/OSmod/python{i}") # create till 9 
except FileExistsError:
    print(f"File exists with {1}")
try:
    for i in range(1, 10):
        os.rename(f"resources/OSmod/python{i}", f"resources/OSmod/osMod_{i}") # rename folders
except FileExistsError:
    print(f"no need of rename")
folders = os.listdir("resources/OSmod/") # returns all folders into a list
for folder in folders:
    print(folder)
    
os.system("dir") # runs cmd in terminal

print(os.getcwd()) # returns the current working directory

try:
    os.remove("resources/OSmod/osMod_1/demo") #  remove file 
except FileExistsError:
    pass

os.rmdir("resources/OSmod/osMod_2") # only removes empty directory