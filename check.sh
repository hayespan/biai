#!/usr/bin/env sh

pyflakes .| grep -v unused| grep -v "never use"

