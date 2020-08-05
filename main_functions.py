__desc__ = "Main functions of the renamer"
__author__ = "Filipe Ligeiro Silva"

import os
from datetime import date
from auxiliary_functions import info_directory

def rename_time(directory):
    files, extension = info_directory(directory)

    today = date.today().strftime("%d.%m.%Y")

    for i, file in enumerate(files, 1):
        os.rename("{}/{}".format(directory, file),\
            "{}/{} ({}){}".format(directory, today, i, extension))

def rename_enumerate(directory):
    files, extension = info_directory(directory)        

    for i, file in enumerate(files, 1):
        os.rename("{}/{}".format(directory, file),\
            "{}/{}{}".format(directory, i, extension))

def rename_extension(directory, extension):
    files, old_ext = info_directory(directory)

    for i in range(len(files)):
        files[i] = os.path.splitext(files[i])[0]

    for file in files:
        os.rename("{}/{}".format(directory, file + old_ext),\
            "{}/{}{}".format(directory, file, extension))