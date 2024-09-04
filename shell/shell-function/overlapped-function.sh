#/bin/bash

function a(){
    function b(){
        echo "b" $@
    }
    echo "a" $@
    b $@
}

a 1 2 3
