import sys
from collections import *
from itertools import *
from math import *

points = []

slope1 = 1
slope2 = 1

Ax, Ay = [int(i) for i in sys.stdin.readline().split()]
Bx, By = [int(i) for i in sys.stdin.readline().split()]
Cx, Cy = [int(i) for i in sys.stdin.readline().split()]

if Bx - Ax != 0:
    slope1 = (By - Ay) / (Bx - Ax)
else:
    slope1 = float("inf")

if Cx - Bx != 0:
    slope2 = (Cy - By) / (Cx - Bx)
else:
    slope2 = float("inf")


if slope1 == slope2:
    print("TOWARDS")
else:
    if Bx > Cx:
        print("LEFT")
    else:
        print("RIGHT")
