import sys
from collections import *
from itertools import *
from math import *

stack = []

for i in range(int(input())):
    cmd = sys.stdin.readline().strip().split()
    
    if len(cmd) == 1:
        if stack:
            print("/" + "/".join(stack)+ "/")
        else:
            print("/")
            
    else:
        directory = cmd[1].split("/")
        directory = [i for i in directory if i != ""]

        if cmd[1][0] == "/":
            stack.clear()
            for path in directory:
                if path == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(path)
        
        else:
            for path in directory:
                if path == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(path)