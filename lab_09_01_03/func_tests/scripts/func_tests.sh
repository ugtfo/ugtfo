#!/bin/bash
len=$(($(find ../data/ -name "pos_[0-9][0-9]*_in.txt" | wc -l)+1))
for ((i = 1; i < len; i++)); do
    ./pos_case.sh "../data/pos_0""$i""_in.txt" "../data/pos_0""$i""_out.txt"
    echo -n "Positive test $i: "
    if [ $? ]; then
        echo "Passed"
    else
        echo "Failed"
    fi
done
len=$(($(find ../data/ -name "neg_[0-9][0-9]*_in.txt" | wc -l)+1))
for ((i = 1; i < len; i++)); do
    ./neg_case.sh "../data/neg_0""$i""_in.txt" "../data/neg_0""$i""_out.txt"
    echo -n "Negative test $i: "
    if [ $? ]; then
        echo "Passed"
    else
        echo "Failed"
    fi
done
rm out.txt
