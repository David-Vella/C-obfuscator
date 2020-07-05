#!/bin/bash

FLAGS="-lncurses"

run_test() {

    local name=$(echo $1 | cut -d'.' -f1)

    echo -n "Running Test $name..."

    cd tests/$name/

    local files=$(ls)

    cd ../../

    cp -r tests/$name/* .

    python -m cobfuscator "$@"

    gcc $FLAGS obfuscated.c > tests/compiler.log 2>&1

    local status="$?"

    rm $files

    if [ $status -ne 0 ]; then
        echo "Failed"
        exit 1

    else
        echo "Passed"
    fi
}

run_test hello.c

run_test tictactoe.c main.c
