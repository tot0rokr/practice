#!/bin/bash


cleanup()
{
    echo "cleanup $1"
}

trap "cleanup $$" SIGTERM

sleep 10
