#!/bin/bash
# usage: g.sh prefix regex [width]
grep -E "^\[$1" dump.txt | grep -iE "$2" | cut -c1-${3:-600}
