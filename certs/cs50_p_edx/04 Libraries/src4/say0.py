# Demonstrates pip-installed package

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.milk("hello, " + sys.argv[1])

