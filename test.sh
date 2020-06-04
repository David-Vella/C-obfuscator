for i in {1..100}; do
    PROGOUT=$(python3 cobfuscator tictactoe.c main.c)
    OUTPUT=$(gcc main.obf.c tictactoe.obf.c -lncurses 2>&1)

    if [[ $OUTPUT == *warning* || $? -ne 0 ]]; then
        echo "$OUTPUT"
        echo "Failed to compile"
        exit 1
    fi
done

echo "Success"