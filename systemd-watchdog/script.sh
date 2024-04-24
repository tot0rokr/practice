#!/bin/bash

event_handler() {
        echo "Run event!"
}


cleanup() {
        systemd-notify STOPPING=1
        systemd-notify --status="Quitting"
        sleep 25s
        exit 0
}

trap "cleanup" SIGTERM
trap "cleanup" SIGABRT


if [ -z $WATCHDOG_PID ] || [ -z $WATCHDOG_USEC ] || [ -z $NOTIFY_SOCKET ]; then
        echo "NO watchdog"
else
        # Use systemd watchdog
        systemd-notify --status="Starting"
        sleep 15s
        systemd-notify READY=1
        systemd-notify --status="Running"

        while true; do
                systemd-notify WATCHDOG=1
                event_handler
                sleep 5s
        done

fi
