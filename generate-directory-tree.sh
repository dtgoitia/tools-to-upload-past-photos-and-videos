#!/bin/bash

directory=$1
# If last character is "/", drop it
directory="${directory%/}"

tree -Q -p --du -h --dirsfirst $directory > "tree-index_${directory}"
