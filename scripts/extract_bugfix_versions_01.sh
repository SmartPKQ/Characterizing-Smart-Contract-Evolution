#!/bin/bash

D=$PWD

cd /data/lpy/ase/repos
for repo in *; do
    echo $repo
    cd $repo
    git log --first-parent --date-order --reverse --pretty='format:%h %s' | awk 'BEGIN {i=1} {print i++, $0}' | grep '[Bb][Uu][Gg]\|[Vv][Uu][Ll][Nn]'
    # git log --first-parent --date-order --reverse --pretty='format:%h %s' | awk 'BEGIN {i=1} {print i++, $0}' | grep '[Gg][Aa][Ss]'
    cd - &> /dev/null
done

cd $D
