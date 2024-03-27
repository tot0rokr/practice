#!/bin/bash

function func1 {
    return 0
}

function func2 {
    return 1
}

function func3 {
    echo "hi"
}

function func4 {
    cat badfile
}


func1
echo "$?"
func2
echo "$?"
func3
echo "$?"
func4
echo "$?"
