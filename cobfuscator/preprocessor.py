import sys, os

from cobfuscator import whitespace

def grab_string(f):
    string = ''
    while True:
        char = f.read(1)

        if not char:
            if len(string):
                break
            else:
                return(False)

        if char in whitespace:
            if len(string):
                return(string)
            else:
                continue
        
        string += char

def process(src, dst):
    definitions = []
    includes = []

    while True:
        string = grab_string(src)
        
        if not string:
            break

        if string == '#include':
            lib = grab_string(src)
            if lib[0] == '\"':
                includes.append(lib.replace('\"', ''))

        if string == '#define':
            definitions.append(grab_string(src))

    print(definitions)
    print(includes)