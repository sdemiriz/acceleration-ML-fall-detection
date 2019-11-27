#!/bin/bash
# by: Sedat Demiriz

# add this to ~/.local/bin on Unix for global access
# Use:
#       numbercsv.sh <new name prefix>
# Ex:
#       numbercsv.sh test               ->          test01.csv, test02.csv etc.

a=1
for i in *.csv; do 
    new=$(printf "%s%02d.csv" "$1" "$a")
    mv -i -- "$i" "$new"
    let a=a+1
done
