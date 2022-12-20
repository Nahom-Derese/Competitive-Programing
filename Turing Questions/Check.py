x = 'abcdef'

i = 'a'

while i in x[:-1]:
    print(i, end='')


inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(inputs)

for i in inputs:
    inputs.append(i)

print(inputs)
