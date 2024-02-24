for i in range(int(input())):
    x = input()
    if x.count('A') < x.count('B'):
        print('B')
    else:
        print('A')