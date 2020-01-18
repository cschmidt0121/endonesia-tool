from shutil import which
import inspect
import os

def read_in_chunks(file_object, chunk_size = 4, size = 0):
    currentsize = 0
    while True:
        data = file_object.read(chunk_size)
        if not data or (size > 0 and size <= currentsize):
            break
        currentsize += chunk_size
        yield data

def csv_find(pointer, csv, text = False):
    size = len(csv)
    for row in range(0, size):
        if pointer == int(csv[row][0]) and (not text or text == int(csv[row][1])):
            return row
    return -1

def check_bin(name):
    return which(name) is not None

tooldir = ''
