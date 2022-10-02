import re
      
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def getCol(s):
    if len(s) == 1:
        return alpha.index(s) + 1
    elif len(s) == 2:
        fi = alpha.index(s[0]) + 1
        si = alpha.index(s[1]) + 1
        return (26 * fi) + si
    elif len(s) == 3:
        fi = alpha.index(s[0]) + 1
        si = alpha.index(s[1]) + 1
        ti = alpha.index(s[2]) + 1
        return (26**2 * fi) + (si * 26) + ti

sps = int(input())
for s in range(sps):
    col, row = [int(x) for x in input().split()]
    if col == 0 or row == 0:
        break
    table = [[0 for x in range(col)] for j in range(row)]

    for i in range(row):
        line = input().split(' ')
        for j in range(len(line)):
            if line[j].isnumeric():
                table[i][j] = int(line[j])
            else:
                s = line[j]
                s = s[1:]
                s = s.split('+')
                sum = 0
                for a in s:
                    both = re.match(r'([A-Z])+([0-9])+', a)
                    alp, rowu = both.groups()
                    rowu = int(rowu) - 1
                    colu = getCol(alp) - 1
                    if rowu < row and colu < col:
                        sum += table[rowu][colu]
                table[i][j] = sum

    for i in range(row):
        print(' '.join([str(x) for x in table[i]]))
  