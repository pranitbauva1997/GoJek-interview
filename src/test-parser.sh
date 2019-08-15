#!/bin/bash

python parser.py <input.txt >out.temp
diff out.temp output.txt

if [ $? -eq 0 ]
then
    echo "Tests Passed :)"
else
    echo "Tests Failed :("
fi
