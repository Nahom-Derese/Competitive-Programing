string = input()

def solution(string):
    x = set()
    unknown = 0
    alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    if len(string) < 26:
        return -1

    if len(string) == 26:
        for i in string:
            if i != '?':
                x.add(i)
                if i in alphabets:
                    alphabets.remove(i)
            else:
                unknown += 1

        if len(x) + unknown == 26:
            replaced = string.replace('?','{}')
            replaced = replaced.format(*alphabets)
            return replaced

        else:
            return -1


    l_ptr = 0
    r_ptr = 26

    while r_ptr <= len(string):
        window = string[l_ptr:r_ptr]
        x = set()
        unknown = 0
        alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        for i in window:
            if i != '?':
                x.add(i)
                if i in alphabets:
                    alphabets.remove(i)
            else:
                unknown += 1

        if len(x) + unknown == 26:
            replaced = window.replace('?','{}')
            replaced = replaced.format(*alphabets)
            left = string[:l_ptr]
            right = string[r_ptr:]
            answer = left + replaced + right
            answer = answer.replace('?', 'A')
            return answer

        l_ptr += 1
        r_ptr += 1

    return -1
    
print(solution(string))
