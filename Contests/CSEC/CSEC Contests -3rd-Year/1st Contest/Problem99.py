import math
a = int(input())
answers = []
milestones = [1]

c = 1
milestones_len = 1
while milestones[-1] < 2147483647:
    c += 1
    d = str(c)
    k = len(milestones)
    if (k > 8):
        inc = milestones[milestones_len-9]

    sumnum = int((c*c + c)/2)
    milestones.append(sumnum)
    milestones_len += 1

newMilestones = []

for j in range(milestones_len):
    length = len(str(j+1))

    if (milestones[j] > 2147483647):
        break

    if milestones[j] > 45:
        newMilestone = milestones[j]

        for k in range(1, length):
            offset = int('9'*k)
            if j - offset >= 0:
                newMilestone += milestones[j-offset]

        newMilestones.append(newMilestone)

        if newMilestone >= 2147483647:
            break
    else:
        newMilestones.append(milestones[j])

for i in range(a):
    b = int(input())

    main = []

    for i in newMilestones:
        main.append(i)
        if i >= b:
            break

    string = ''
    for i in range(1, len(main) + 1):
        string += str(i)

    answers.append(string[b-main[-1]-1])

for i in answers:
    print(i)
