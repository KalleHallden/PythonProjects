
import os
import sys

path = os.getcwd()

i = 0
folders = {}
main_folder = ""

for subdir, dirs, files in os.walk(path):
    dir_name = str(subdir).split("/")
    dir_name = dir_name[len(dir_name)-1]
    
    if len(main_folder) < 1:
        main_folder = dir_name 
    folders_and_files = []

    for dir_ in dirs:
        folders_and_files.append(dir_)
    for file_ in files:
        folders_and_files.append(file_)
    
    folders[dir_name] = folders_and_files

final_list = []

def recursive_tree(folder, num):
    files = ""
    num = num + "-"
    try:
        files = folders[folder]
        return go_through_list(files, len(files)-1, num)
    except:
        Exception()

def go_through_list(list_, index, num):
    if len(num) == 2:
        final_list.append(str(list_[index]))
    else:
        final_list.append(num + " " + str(list_[index]))
    if index == 0:
        recursive_tree(list_[index], num)
        return 
    else:
        recursive_tree(list_[index], num)
        return go_through_list(list_, index - 1, num)    

recursive_tree(main_folder, " ")

for item in final_list:
    print(item) 
