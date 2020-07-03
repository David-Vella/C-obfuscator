import sys, os, json

with open('cobfuscator/cthings.json') as cthings_file:
    cthings = json.load(cthings_file)

whitespace = cthings['whitespace']
operators = cthings['operators']
delimiters = whitespace + operators + cthings['other']

class token:
    def __init__(self, string='', family=None):
        self.string = string
        self.family = family

    def __repr__(self):
        return('{} : {}'.format(self.family, self.string))

    def __len__(self):
        return(len(self.string))

    def __add__(self, other):
        try:
            return(self.string + other)
        except AttributeError:
            return(self.string + other.string)


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
            char += grab_until(f, '\"')
        if char == '\'':
            char += grab_until(f, '\'')

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

def string_list(src):

    result = []

    out = grab_token(src)

    while out:

        if out[:1] == '#':

            out += grab_until(src, '\n')
            result.append(out.strip())
        
        else:
            result.append(out)

        out = grab_token(src)

    return(result)

def token_list(src):

    result = []

    out = grab_token(src)

    while out:

        if out[:1] == '#':

            out += grab_until(src, '\n')
            result.append(out.strip())
        
        else:
            result.append(out)

        out = grab_token(src)

    return(result)

def tokenize(src, dst):
    while True:
        out = grab_token(src)

        if not out:
            break

        elif out[:8] == '#include': #handle in tokenize?
            next_token = grab_token(src)
            if next_token == '<':
                next_token += grab_token(src) + grab_token(src)
            out += ' ' + next_token
            dst.write('{}\n'.format(out))

        # ignore macros
        elif out[:7] == '#define': # tripped up by inline comments
            while True:
                if src.read(1) == '\n':
                    break
                else:
                    src.seek(src.tell() - 1, os.SEEK_SET)
                    next_token = grab_token(src)
                    if next_token != '(':
                        out += ' '
                    out += next_token
            dst.write('{}\n'.format(out))
        
        elif out[:1] == '#':
            out += grab_until(src,'\n')
            dst.write(out)

        else:
            dst.write('{}\n'.format(out))
            