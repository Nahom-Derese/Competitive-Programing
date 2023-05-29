a = int(input())

answers = []

for i in range(a):
    b = int(input())
    c = 1

    milestones = [1]

    while milestones[len(milestones)-1] <= b:
        c += 1
        sumnum = int(((c)/2) * (c+1))
        milestones.append(sumnum)

    resetNum = milestones.pop()
    resetNum = milestones.pop()

    if (b - resetNum == 0):
        num = len(milestones)
        answers.append(num+1)
        continue

    num = b - resetNum
    answers.append(num)

for k in answers:
    print(k)
