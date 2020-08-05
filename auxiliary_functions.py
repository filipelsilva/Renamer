__desc__ = "Auxiliary functions of the renamer"
__author__ = "Filipe Ligeiro Silva"

import os

def info_directory(directory):
    files = os.listdir(directory)

    _, extension = os.path.splitext(files[0])

    return files, extension

# def check_for_date(name):
#     if 