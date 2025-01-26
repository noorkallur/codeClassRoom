# # https://www.w3schools.com/python/python_file_handling.asp

# # READ()
# try:
#     f = open(r"C:\Users\noor.kallur\Perforce\python\Practice\resources\demoReadFile", "rt")
#     print(f)
#     try:
#         print(f.readlines())
#     except:
#         print(f"something went wrong")
#     finally:
#         f.close()
# except FileNotFoundError:
#     print(f'file is not present')
# # use these in the try block individually
# # print(f.read()) # read all the lines in the text file till the end (file object 'f' points to the end)
# # print(f.read(6))# read only the number of characters in the file (f points to the 7th charcter)
# # print(f.readline()) # reads the line till \n (f points to the next line begining)
# # print(f.readlines()) #  method returns a list containing each line in the file as a list item.(f points to the end)
# # print(f.readlines(12)) # for the file provided this return 3 lines( as two lines size is 10) # f.readlines(maxSize) -> iterate through file until the number of characters is more than maxSize provided

# # WRTIE()
# # https://www.w3schools.com/python/python_file_write.asp
# # "a" - Append - will append to the end of the file, create  the file if not present
# # "w" - Write - will completly overwrite any existing content, create the file if not present
# f = open(r"C:\Users\noor.kallur\Perforce\python\Practice\resources\demoWriteFile", "a") # append
# name = input("Enter your name: ")
# f.write(f"addding the content at the end of the line with(not next line) {name}")
# f.close()
# f = open(r"C:\Users\noor.kallur\Perforce\python\Practice\resources\demoWriteFile2", "w") # write
# f.write("Woops! I have deleted the content! again!")
# f.close()

# # using WITH statement automatically closes the file
# with open(r"C:\Users\noor.kallur\Perforce\python\Practice\resources\demoWriteFile2", "a") as f:
#     f.write("appending line")
    
# #wap reading postion data from a file pos = { x, y, z}
# with open(r"C:\Users\noor.kallur\Perforce\python\Practice\resources\position_data", "rt") as f:
#     i = 0
#     while True:
#         i = i + 1
#         line = f.readline()
#         print(f"line->{line}")
#         if not line: # line will be empty at the end of the file so use it to break from loop
#             break
#         x = line.split(",")[0] # split returns a list of items with the seperator, better way to do-> x, y , z = line.split(",")
#         y = line.split(",")[1]
#         z = line.split(",")[2]
#         print(f"postion {i} [{x}, {y}, {z}]")

# # seek(int) -> f goes to the postion
# # tell() -> f returns the postion
# # truncate(int) -> f truncates till input bytes 