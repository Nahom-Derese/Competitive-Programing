a = input()

currentNumber = 0

summation = 0

for i in a:
    if i=='O':
        currentNumber += 1
        summation += currentNumber
    else:
        currentNumber = 0

print(summation)