import sys
from collections import defaultdict

n, m = [int(i) for i in sys.stdin.readline().split()]
count = defaultdict(int)

for i in range(m):
    node1, node2 = [int(i) for i in sys.stdin.readline().split()]
    count[node1]+=1
    count[node2]+=1
    
if len(set(count.values())) == 1:
    print("YES")
else:
    print("NO")