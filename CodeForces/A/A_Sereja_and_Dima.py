ptr_1 = 0
ptr_2 = int(input()) - 1

inputlist = [int(i) for i in input().split()]

serj = 0
dima = 0

clk = 0

while ptr_1 <= ptr_2:
    if clk % 2 == 0:
        if inputlist[ptr_1] > inputlist[ptr_2]:
            serj += inputlist[ptr_1]
            ptr_1 += 1
        else:
            serj += inputlist[ptr_2]
            ptr_2 -= 1
    else:
        if inputlist[ptr_1] > inputlist[ptr_2]:
            dima += inputlist[ptr_1]
            ptr_1 += 1
        else:
            dima += inputlist[ptr_2]
            ptr_2 -= 1
    
    clk += 1

print(serj, dima)