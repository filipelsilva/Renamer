__desc__ = "Auxiliary functions of the renamer"
__author__ = "Filipe Ligeiro Silva"

import os, re

def info_directory(directory, mode):
    files = os.listdir(directory)
    _, extension = os.path.splitext(files[0])

    if wrong_extension(extension):
        extension = ""
    
    if mode == True:
        names = []

        for el in files:
            names.append(os.path.splitext(el)[0])
        
        return files, names, extension
        
    return files, extension

def wrong_extension(name):
    pattern = "[.]\d\d\d\d[ ][(]\d+[)]"

    if re.findall(pattern, name) == []:
        return False
    
    return True
