#!/bin/bash

# Check if the current script was called directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "ERROR: Script called directly. Use 'source' to call this script."
    echo 'RUN => source ./aliash.sh'
    exit 1
fi

alias mmtran="python transfer.py"
alias mmrewrite="python rewrite_names.py"

echo "Set media manager aliases"