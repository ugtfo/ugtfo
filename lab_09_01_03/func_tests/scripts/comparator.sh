#!/bin/bash
test=$(grep -Eo "(-?)[0-9]+\.[0-9]+" "$1")
res=$(grep -Eo "(-?)[0-9]+\.[0-9]+" "$2")
if [ "$test" = "$res" ]; then
    exit 0;
else
    exit 1;
fi