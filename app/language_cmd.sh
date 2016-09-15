#!/usr/bin/env sh

cmd="$1"

if [ $cmd = "pot" ]; then
    pybabel extract -F babel.cfg -o messages.pot .
elif [ $cmd = "crpo" ]; then
    pybabel init -i messages.pot -d translations -l $2
elif [ $cmd = "udpo" ]; then
    pybabel update -i messages.pot -d translations
elif [ $cmd = "cmp" ]; then
    pybabel compile -d translations
fi

