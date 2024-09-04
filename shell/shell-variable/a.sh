#!/bin/bash

a=10

echo $a

echo $(a=20 ./b.sh)

echo $b
echo $a

echo $@
