x = int(input())

Ans = []

for i in range(x):
    Answer = 0
    Moves = []
    n = int(input())
    for j in range(n):
        ac = input()
        if ac == "LEFT":
            Answer -= 1
            Moves.append(-1)
        elif ac == "RIGHT":
            Answer += 1
            Moves.append(1)
        for i in range(len(Moves)):
            y = "SAME AS {0}".format(i+1)
            if ac == y:
                if Moves[i] == -1:
                    Answer -= 1
                    Moves.append(-1)
                else:
                    Answer += 1
                    Moves.append(1)
    Ans.append(Answer)

for u in Ans:
    print(u)