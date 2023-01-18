
def gibo(n,x,y):
    # After trying to solve this problem by a recursive solution, I realized that the pattern is a repeating pattern of 6 numbers
    # I realized this pattern by generating the first 100 numbers of the sequence and noticed that the pattern repeats itself
    # the pattern is straight forward
    # if the remainder of n/6 is 0, then the number is x
    if n%6 == 0:
        return x
    # if the remainder of n/6 is 1, then the number is y
    if n%6 == 1:
        return y
    # if the remainder of n/6 is 2, then the number is y-x
    if n%6 == 2:
        return y-x
    # if the remainder of n/6 is 3, then the number is -x
    if n%6 == 3:
        return -x
    # if the remainder of n/6 is 4, then the number is -y
    if n%6 == 4:
        return -y
    # if the remainder of n/6 is 5, then the number is x-y
    else:
        return x-y
    