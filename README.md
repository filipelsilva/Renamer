# Renamer (version 0.3)

A program to batch rename your files, written in Python3, made by Filipe Ligeiro Silva

## Usage

```text
python3 renamer.py [-h] [-t | -n | -e] -d
```

### Modes

```text
-h, --help: help about the program
-t, --time: rename files with the current date, followed by (<number>)
-n, --enum: rename files by number (1, 2, 3, ...)
-e, --ext: renames the extension of the files (has to be given an argument, the new extension, starting with a do)
```

### Variables

```text
-d, --dir: directory to rename
```

## Usage examples (command mode only)

### Renaming by date

```bash
python3 renamer.py -t -d <directory>
```

### Renaming by enumeration

```bash
python3 renamer.py -n -d <directory>
```

### Renaming the extension

```bash
python3 renamer.py -e .<extension> -d <directory>
```
