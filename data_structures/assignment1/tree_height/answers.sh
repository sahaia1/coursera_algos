#!/bin/bash
ls tests | grep a | awk '{ print "cat tests/"$1 }' | bash > actual_answers.txt
ls tests | grep -v a | awk '{ print "python3 tree-height.py < tests/"$1 }'| bash > answers.txt
vimdiff answers.txt actual_answers.txt