a = int(input())

def even(integer):
    return integer % 2 == 0

for i in range(a):
    string = input()

    if len(string) == 1:
        print(string)
        continue

    first_ptr=0
    second_ptr=1

    ans = []

    while second_ptr < len(string):
        if string[first_ptr] in ans:
            first_ptr += 1
            second_ptr = first_ptr
            continue

        if string[first_ptr] == string[second_ptr]:
            if second_ptr == len(string) - 1:
                if even((second_ptr) - first_ptr):
                    ans.append(string[first_ptr])
                break
            second_ptr += 1
        else:
            if even((second_ptr-1) - first_ptr):
                ans.append(string[first_ptr])
            first_ptr = second_ptr
    
    ans.sort()

    for i in ans:
        print(i, end="")
    
    print()