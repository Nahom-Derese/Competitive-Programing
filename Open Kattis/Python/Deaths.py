shares = 0
crowns = 0
average = 0

while True:
    a = input()
    b = a.split()

    if b[0] == "die":
        profit = int(b[1]) - average
        if(profit < 0):
            print(shares * ( int(b[1]) ) )
        else:
            print(shares * ( int(b[1]) - (profit * 0.3) ) )
        break
    else:
        if b[0] == "buy":
            shares += int(b[1])
            crowns += int(b[1]) * int(b[2])
            average = crowns
            average /= shares
        if b[0] == "split":
            shares *= int(b[1])
            average /= int(b[1])
        if b[0] == "sell":
            shares -= int(b[1])
        if b[0] == "merge":
            shares //= int(b[1])
            average *= int(b[1])



