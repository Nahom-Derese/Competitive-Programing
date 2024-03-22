import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    m = 0
    def rec(n):
        nonlocal m
        if n == m:
            return True
        if n < m or n % 3:
            return False
        
        return rec(n // 3) or rec(n - (n//3))
        
    for i in range(int(input())):
        n , m = [int(i) for i in input().split()]

        if rec(n):
            print("YES")
        else:
            print("NO")
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

