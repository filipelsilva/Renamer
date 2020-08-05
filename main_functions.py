__desc__ = "Main functions of the renamer"
__author__ = "Filipe Ligeiro Silva"

import os
from datetime import date
from auxiliary_functions import info_directory

def rename_time(directory):
    files, extension = info_directory(directory, 0)

    today = date.today().strftime("%d.%m.%Y")

    for i, file in enumerate(files, 1):
        os.rename("{}/{}".format(directory, file),\
            "{}/{} ({}){}".format(directory, today, i, extension))

def rename_enumerate(directory):
    files, extension = info_directory(directory, 0)        

    for i, file in enumerate(files, 1):
        os.rename("{}/{}".format(directory, file),\
            "{}/{}{}".format(directory, i, extension))

def rename_extension(directory, extension):
    files, names, _ = info_directory(directory, 1)

    for file, name in zip(files, names):
        os.rename("{}/{}".format(directory, file),\
            "{}/{}{}".format(directory, name, extension))