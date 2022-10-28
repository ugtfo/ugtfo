#!/bin/bash
if [ "$USE_VALGRIND" ]; then
  valgrind --log-file=valgrind_out.txt
  ../../app.exe "$3" < "$1" > out.txt
else
  ../../app.exe "$3" < "$1" > out.txt
fi
if [ $? ]; then
    exit 1
else
    exit 0
fi
