#!/bin/bash

FLAGS="-Werror -Wall -lncurses"

run_test() {

    local name=$(echo $1 | cut -d'.' -f1)

    echo -n "Running Test $name..."

    cd tests/$name/

    local files=$(ls)

    cd ../../

    cp -r tests/$name/* .

    python cobfuscator "$@"

    gcc $FLAGS out.c > tests/compiler.log 2>&1

    if [ $? -ne 0 ]; then
        echo "Failed"

        rm $files

        exit 1

    else
        echo "Passed"
    fi

    rm $files
}

run_test hello.c

run_test tictactoe.c main.c
