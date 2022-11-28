#!/bin/sh
set -e
filename=$1
[ -z "${filename}" ] && filename=test
./main.py > ${filename}.mml
mml2mid ${filename}.mml ${filename}.mid
timidity -Ow -o ${filename}.wav ${filename}.mid
echo "output: ${filename}.wav"
