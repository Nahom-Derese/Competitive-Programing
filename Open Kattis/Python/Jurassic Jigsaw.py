def dif(a, b):
    count = 0
    for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
    return count

a, b = input().split()

a = int(a)
b = int(b)
c = []
maping = []

for i in range(a):
    c .append(input())
for j in range(len(c)):
    for k in range(j,len(c)):
        if k == j:
            continue
        else:
            maping.append("{} {} {}".format(j, k, dif(c[j], c[k])))


maping.sort(key=(lambda x: int(x.split()[2])))
sum = 0
for i in range(len(maping[:a-1])):
    sum += int(maping[i].split()[2])
    print(maping[i].split()[0], maping[i].split()[1])
            

print(sum)
