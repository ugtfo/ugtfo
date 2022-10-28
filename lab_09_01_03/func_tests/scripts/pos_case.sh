#!/bin/bash
if [ "$USE_VALGRIND" ]; then
  valgrind --log-file=valgrind_out.txt
  ../../app.exe "$3" < "$1" > out.txt
else
  ../../app.exe "$3" < "$1" > out.txt
fi
if ./comparator.sh out.txt "$2"; then
  exit 0
else
  exit 1
fi
