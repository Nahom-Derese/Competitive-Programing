import sys

def pow_two(n):
    return n > 0 and 2**20 % n == 0


for i in range(int(input())):
    num = int(sys.stdin.readline())
    
    if not pow_two(num):
        print("YES")
    else:
        print("NO")