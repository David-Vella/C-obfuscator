import sys, os, json, re, random
import string as string_things

with open('cobfuscator/cthings.json') as cthings_file:
    cthings = json.load(cthings_file)

whitespace = cthings['whitespace']
operators = cthings['operators']
symbols = cthings['symbols']
delimiters = whitespace + operators + symbols
types = cthings['types']
keywords = types + cthings['keywords']

class Token:
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

    STRING_LITERAL = 'string literal'
    CHAR_LITERAL = 'char literal'
    INT_LITERAL = 'int literal'
    FLOAT_LITERAL = 'float literal'

    CONSTANT = 'constant'
    NAME = 'name'
    DIRECTIVE = 'directive'

    SYMBOL = 'symbol'
    KEYWORD = 'keyword'
    TYPE = 'type'
    OPERATOR = 'operator'

    LIBRARY = 'library defined'


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

    tokens = []
    names = []

    for string in string_list(src):
        tokens.append(Token(string=string))

    for i in range(len(tokens)):
        if tokens[i].string in names:
            tokens[i].family = Token.NAME

        elif tokens[i].string[:1] == '#':
            tokens[i].family = Token.DIRECTIVE

        elif tokens[i].string[0] == '\"' and tokens[i].string[-1] == '\"':
            tokens[i].family = Token.STRING_LITERAL
            
        elif tokens[i].string[0] == '\'' and tokens[i].string[-1] == '\'':
            tokens[i].family = Token.CHAR_LITERAL

        elif re.search('^[0-9]+$', tokens[i].string) or \
             re.search('^(0x)[0-9a-f]+$', tokens[i].string) or \
             re.search('^(0b)[01]+$', tokens[i].string):
            tokens[i].family = Token.INT_LITERAL

        elif re.search('^[0-9]+[.][0-9]+$', tokens[i].string):
            tokens[i].family = Token.FLOAT_LITERAL

        elif tokens[i].string in types:
            tokens[i].family = Token.TYPE

        elif tokens[i].string in keywords:
            tokens[i].family = Token.KEYWORD

        elif tokens[i].string in symbols:
            tokens[i].family = Token.SYMBOL

        elif tokens[i].string in operators:
            tokens[i].family = Token.OPERATOR

        elif tokens[i].string != tokens[-1].string != tokens[0].string:
            offset = 1
            while tokens[i - offset].string == '*':
                offset += 1
            if tokens[i - offset].family == Token.TYPE:
                tokens[i].family = Token.NAME
                names.append(tokens[i].string)

            else:
                tokens[i].family = Token.LIBRARY

    return(tokens)


def tokenize(src, dst):
    while True:
        out = grab_token(src)

        if not out:
            break

        elif out[:1] == '#':
            out += grab_until(src,'\n')
            dst.write(out)

        else:
            dst.write('{}\n'.format(out))
