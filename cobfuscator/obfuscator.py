import sys, os, string, random

from cobfuscator import process, token_list, Token

def generate_name(length=4):
    letters = string.ascii_lowercase

    name = []
    
    for _i in range(length):
        name.append(random.choice(letters))

    return(''.join(name))

def handle_string(string):
    if '\\x' in string:
        return(string)

    result = ['\"']

    escape = { 'n' : '\n', 't' : '\t' }

    for i in range(len(string)):
        if string[i] == '\"':
            continue
        elif string[i] == '\\' and string[i - 1] != '\\':
            continue
        elif string[i - 1] == '\\':
            num = str(hex(ord(escape[string[i]]))).replace('0x', '')
        else:
            num = str(hex(ord(string[i]))).replace('0x', '')

        result.append('\\x{}'.format(num))
    
    result.append('\"')

    return(''.join(result))

def obfuscate(src, dst):
    tokens = token_list(src)

    line = []

    names = {}

    for token in tokens:
        if token.family == Token.DIRECTIVE:
            tokens.remove(token)
            tokens.insert(0, token)

    for i in range(len(tokens)):
        if tokens[i].family == Token.INT_LITERAL:
            tokens[i].string = hex(int(tokens[i].string))

        elif tokens[i].family == Token.CHAR_LITERAL:
            tokens[i].string = hex(ord(tokens[i].string.replace('\'', '')))

        elif tokens[i].family == Token.STRING_LITERAL:
            tokens[i].string = handle_string(tokens[i].string)

        elif tokens[i].family == Token.NAME:
            if tokens[i].string not in list(names.keys()):
                name = generate_name()
                while name in list(names.keys()):
                    name = generate_name()
                names[tokens[i].string] = name

            tokens[i].string = names[tokens[i].string]

        if tokens[i].family == Token.DIRECTIVE:
            dst.write('{}\n'.format(tokens[i].string))
            continue

        line.append('{}'.format(tokens[i].string))

        length = 0
        for string in line:
            length += len(string)
        
        if length > 70:
            dst.write('{}\n'.format(' '.join(line)))
            line.clear()

    dst.write('{}\n'.format(' '.join(line)))

def main():
    sys.argv.pop(0)
    src_files = sys.argv
        
    with open('out.c', mode='w', encoding='utf-8') as out:
        process(src_files, out)

    with open('out.c', mode='r', encoding='utf-8') as src:
        with open('obfuscated.c', mode='w', encoding='utf-8') as dst:
            obfuscate(src, dst)

    os.remove('out.c')

if __name__ == "__main__":
    main()
