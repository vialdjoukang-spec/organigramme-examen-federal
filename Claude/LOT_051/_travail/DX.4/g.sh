#!/bin/bash
# usage: g.sh file regex [maxchars]
grep -iE "$2" /home/user/wt/lot-051/Claude/LOT_051/_travail/DX.4/tx/$1.txt | cut -c1-${3:-900}
