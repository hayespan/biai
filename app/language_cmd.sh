#!/usr/bin/env sh

cmd="$1"

if [ $cmd = "pot" ]; then
    pybabel extract -F babel.cfg -o ./language/messages.pot .
elif [ $cmd = "crpo" ]; then
    pybabel init -i ./language/messages.pot -d ./language/translations -l $2
elif [ $cmd = "udpo" ]; then
    pybabel update -i ./language/messages.pot -d ./language/translations
elif [ $cmd = "cmp" ]; then
    pybabel compile -d ./language/translations
fi

