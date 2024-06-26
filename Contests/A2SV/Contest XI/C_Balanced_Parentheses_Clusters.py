import sys
from collections import *
from itertools import *
from math import *

class DSU:
    def __init__(self, size):
        self.parent = {i:i for i in range((size+1))}
        self.size = [1] * (size+1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False

        if self.size[parent_x] < self.size[parent_y]:
            self.parent[parent_x] = parent_y
            self.size[parent_y] += self.size[parent_x] 
        else:
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y] 
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)



def solve_problem(brackets):
    stack = []
    dsu = DSU(len(brackets))

    for i in range(len(brackets)):
        b = brackets[i]
        n = len(brackets)
        if b == "(":
            stack.append(i+1)
        else:
            index = stack.pop()
            dsu.union(index, i+1)
            
    # for i in range(1, len(brackets)):
    #     if brackets[i-1] == ")" and brackets[i] == "(":
    #         dsu.union(i, i+1)

    visit = set()
    for i in range(len(brackets)):
        visit.add(dsu.find(i+1))
    
    return len(visit)

if __name__ == '__main__':
    for i in range(int(input())):
        open_brackets = int(sys.stdin.readline().strip())
        brackets = sys.stdin.readline().strip()
        
        print(solve_problem(brackets))

    