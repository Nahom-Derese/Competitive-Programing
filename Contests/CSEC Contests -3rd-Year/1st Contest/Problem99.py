import math

a = int(input())

answers = []

for i in range(a):
    b = int(input())
    c = 1

    milestones = [1]
    mile = []
    inc = 0
    while milestones[len(milestones)-1] < b:
        c += 1
        d = str(c)
        k = len(milestones)
        if (k > 8):
            inc = milestones[k-9]

        sumnum = int((c*c + c)/2)

        milestones.append(sumnum)

    newMilestones = []

    for j in range(len(milestones)):
        length = len(str(j+1))

        if milestones[j] > 45:
            newMilestone = milestones[j]

            for k in range(1, length):
                offset = int('9'*k)
                if j - offset >= 0:
                    newMilestone += milestones[j-offset]

            newMilestones.append(newMilestone)

            if newMilestone >= b:
                break
        else:
            newMilestones.append(milestones[j])

    string = ''
    for i in range(1, len(newMilestones) + 1):
        string += str(i)

    answers.append(string[b-newMilestones[-1]-1])

for i in answers:
    print(i)
