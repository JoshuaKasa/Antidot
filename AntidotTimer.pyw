from time import sleep
from subprocess import call

min: int = 60 * 3

while min > 0:
    min -= 1

    if min == 0:
        call(["AntidotDestruction.cpp"])
        break