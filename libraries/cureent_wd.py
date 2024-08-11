import os


def current_directory():
    cwd = os.getcwd()
    print(cwd)  #Current Working Directiory 


def file_path(filename):
    path = os.path.abspath(filename)
    print(path)     #


current_directory()  #Function Call for Current directory

file_path("even.py")   #Functio call for File name Working directory file
