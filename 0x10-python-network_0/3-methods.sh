#!/bin/bash
# Send an OPTIONS request to the server and display allowed methods
curl -sI -X OPTIONS "$1" | grep -i allow | cut -d ' ' -f2-
