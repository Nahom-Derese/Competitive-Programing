import sys

while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break