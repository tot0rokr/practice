#!/bin/bash


cleanup()
{
    echo "cleanup $1"
    exit 0
}

trap "cleanup $$" SIGTERM
trap "cleanup $$" SIGINT

sleep 10
