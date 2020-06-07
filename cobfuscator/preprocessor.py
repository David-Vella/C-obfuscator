import sys, os

def glob(src_files, dst_file):
    with open(dst_file, mode='w', encoding='utf-8') as dst:
        included = []

        for src in src_files:

            with open(src, mode='r', encoding='utf-8') as src:

                for line in src:

                    line = line.strip()

                    if line[:8] == '#include':

                        if line not in included:

                            included.append(line)

                            if '<' not in line:
                                line = line.split()[1]
                                line = line.replace('\"','')
                                line = line.replace('\n','')
                                dump(line, dst, included)
                            else:
                                dst.write(line + '\n')
                    else:
                        dst.write(line + '\n')

def dump(src_file, dst, ignore=[]):
    with open(src_file, 'r') as src:

        for line in src:

            line = line.strip()

            if line not in ignore:

                dst.write(line + '\n')

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

    print(defined)
    print(definitions)