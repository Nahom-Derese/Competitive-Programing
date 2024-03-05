import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    
    def calculate(s):
        p1 = 0
        p2 = 0
        p1_rem = 5
        p2_rem = 5
        for i in range(10):
            # print(p1, p2)
            if i%2 == 0:
                p1+=int(s[i])
                p1_rem-=1
            else:
                p2+=int(s[i])
                p2_rem-=1
            if (p1 > p2 and p1 - p2 > p2_rem) or (p1 < p2 and p2 - p1 > p1_rem):
                return i+1
        return 10
                

    for i in range(int(input())):
        s = input()


        bais1 = []
        bais2 = []

        for i in range(len(s)):
            if s[i] == "?":
                if i % 2:
                    bais1.append("0")
                else:
                    bais1.append("1")
            else:
                bais1.append(s[i])
        
        for i in range(len(s)):
            if s[i] == "?":
                if i % 2:
                    bais2.append("1")
                else:
                    bais2.append("0")
            else:
                bais2.append(s[i])

        print(min(calculate(bais1), calculate(bais2)))


    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


    