def solution(s):
    b = s.split()

    b.sort(key=lambda item: item[-1])

    for i in b:
        print(i[:-1], end=" ")
    

solution("red2 blue5 black4 green1 gold3")
solution("gold black1 white3 green1 gold3")