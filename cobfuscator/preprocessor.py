import sys, os

from .lexer import tokenize

def uncomment(src, dst):

    line = []

    while True:
        char = src.read(1)
        
        if not char:
            dst.write(''.join(line))
            return

        if char == '/': 
            next_char = src.read(1)
            src.seek(src.tell() - 1, os.SEEK_SET)

            if next_char == '*':

                while char + next_char != '*/':
                    char = next_char
                    next_char = src.read(1)

                continue

            if next_char == '/':

                while char and char != '\n':
                    char = src.read(1)

                continue

        line.append(char)

        if char == '\n':
            dst.write(''.join(line))
            line.clear()

def glob(src_files, dst):

    included = []

    for src_file in src_files:

        name, ext = src_file.split('.')
        dst_file = f'{name}.tmp.{ext}'

        with open(src_file, mode='r', encoding='utf-8') as src_com:

            with open(dst_file, mode='w', encoding='utf-8') as dst_com:

                uncomment(src_com, dst_com)

        with open(dst_file, mode='r', encoding='utf-8') as src:

            for line in src:
                
                line = line.strip()

                if line[:8] == '#include':

                    if line not in included:

                        included.append(line)

                        if '<' not in line:

                            line = line.split()[1]
                            line = line.replace('\"','').replace('\n','')

                            files = [line]
                            glob(files, dst)

                        else:
                            dst.write(line + '\n')

                else:
                    dst.write(line + '\n')

        os.remove(dst_file)

def process(src_files, dst):
    glob_file = 'glob.c'
    token_file = 'tokens.c'

    with open(glob_file, mode='w', encoding='utf-8') as glb:
        glob(src_files, glb)

    with open(token_file, mode='w', encoding='utf-8') as d:
        with open(glob_file, mode='r', encoding='utf-8') as s:
            tokenize(s, d)

    with open(token_file, mode='r', encoding='utf-8') as src:
        definitions = {}
        defined = []

        for line in src:

            line = line.strip()

            while line in list(definitions.keys()):
                line = definitions[line]

            if line[:7] == '#define':

                if len(line.split()) == 2:
                    defined.append(line.split()[1])
                else:
                    key = line.split()[1]

                    val = line.split()[2:]
                    val = ' '.join(val)

                    definitions[key] = val

                continue

            if line[:6] == '#ifdef':
                line = line.split()[1]
                if line not in defined:
                    while line.strip() != '#endif':
                        line = src.readline()
                continue

            if line[:7] == '#ifndef':
                line = line.split()[1]
                if line in defined:
                    while line.strip() != '#endif':
                        line = src.readline()
                continue

            if line[:6] == '#undef':
                line = line.split()[1]
                if line in defined:
                    defined.remove(line)
                continue

            if line[:6] == '#endif':
                continue

            dst.write(line + '\n')

    os.remove('tokens.c')
    os.remove('glob.c')
