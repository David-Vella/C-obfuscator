import sys, os, lexer

def uncomment(src, dst):

    line = ''

    while True:
        char = src.read(1)
        
        if not char:
            dst.write(line)
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

        line += char

        if char == '\n':
            dst.write(line)
            line = ''

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

                if line[:8] == '#include' and line not in included:

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

def process(src):
    definitions = {}
    defined = []

    for line in src:

        line = line.strip()

        if line[:7] == '#define':

            if len(line.split()) == 2:
                defined.append(line.split()[1])
            else:
                key = line.split()[1]
                val = line.split()[2]

                definition = line.split()[3:]

                for string in definition:
                    val += ' ' + string

                definitions[key] = val

    # with open('processed.c', mode='w', encoding='utf-8') as dst:

    # with open('processed.c', mode='w', encoding='utf-8') as dst:
        
    #     for line in src:



    # print(defined)
    # print(definitions)