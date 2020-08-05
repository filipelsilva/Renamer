__desc__ = "Bulk renamer"
__author__ = "Filipe Ligeiro Silva"

import argparse
import os

from main_functions import rename_time, rename_enumerate, rename_extension

if __name__ == "__main__":
    help = "Check the README.md file"
    parser = argparse.ArgumentParser(description=help)
    functions = parser.add_mutually_exclusive_group()

    functions.add_argument("-t", "--time", action="store_true")
    functions.add_argument("-n", "--enum", action="store_true")
    functions.add_argument("-e", "--ext", action="store", dest="extension")

    parser.add_argument("-d", "--dir", action="store",\
        dest="directory", required=True)

    args = parser.parse_args()
    directory = args.directory
    extension = args.extension

    if not os.path.exists(directory):
        print("directory ERROR")
        exit() 

    if args.time:
        rename_time(directory)
    
    if args.enum:
        rename_enumerate(directory)
    
    if args.extension is not None:
        rename_extension(directory, extension)