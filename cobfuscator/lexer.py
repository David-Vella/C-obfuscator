import sys, os

from cobfuscator import whitespace, delimiters, operators

def grab_until(f, delimiter, offset=0):
    '''
    Returns a string 

    offset moves the file start position backwards in f
    
    Moves the file pointer forward in file f
    '''
    string = ''
    f.seek(f.tell() - offset, os.SEEK_SET)
    while True:
        char = f.read(1)
        string += char
        if string[-len(delimiter):] == delimiter:
        #if char == delimiter:
            break
    return(string)

def grab_token(f):
    '''
    Returns a string containing the next token from file f

    Moves the file pointer forward in file f
    '''
    string = ''

    while True:
        char = f.read(1)

        if not char:
            if len(string):
                break
            else:
                return(False)

        # string literal handler
        if char == '\"':
            char += grab_until(f, '\"') #!!! f was src

        if char in delimiters:

            # comment handler
            if char == '/': 
                next_char = f.read(1)
                f.seek(f.tell() - 1, os.SEEK_SET)
                if next_char == '*':
                    grab_until(f, '*/')
                    continue
                if next_char == '/':
                    grab_until(f, '\n')
                    continue

             # operator handler
            if char in operators and not len(string):
                next_char = f.read(1)
                if char + next_char in operators:
                    char += next_char
                    next_char = f.read(1)
                    if char + next_char in operators:
                        char += next_char
                    else:
                        f.seek(f.tell() - 1, os.SEEK_SET)
                else:
                    f.seek(f.tell() - 1, os.SEEK_SET)
            
            # ignore whitespace
            if len(string): 
                f.seek(f.tell() - 1, os.SEEK_SET)
                break
            else:
                if char in whitespace:
                    continue
                else:
                    string += char
                    break
        else:
            string += char
    return(string)

def tokenize(src, dst):
    while True:
        out = grab_token(src)

        if not out:
            break

        # ignore macros
        elif out[0] == '#':
            out += grab_until(src, '\n')

        dst.write('{} '.format(out))