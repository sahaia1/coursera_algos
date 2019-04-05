#!/bin/bash
ls tests | grep a | awk '{ print "echo " $1 ";cat tests/"$1 }' | bash > actual_answers.txt
ls tests | grep -v a | awk '{ print "echo " $1 ".a;python3 process_packages.py < tests/"$1 }'| bash > answers.txt
vimdiff answers.txt actual_answers.txt