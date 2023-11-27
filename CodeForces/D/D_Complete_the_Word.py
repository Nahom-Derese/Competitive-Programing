from string import ascii_uppercase

string = input()

def solution(string):
    x = set()

    l_ptr = 0
    r_ptr = 26

    while r_ptr <= len(string):
        window = string[l_ptr:r_ptr]
        x = set()
        unknown = 0
        alphabets = list(ascii_uppercase)

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
            answer = answer.replace('?', 'Z')
            return answer

        l_ptr += 1
        r_ptr += 1

    return -1
    
print(solution(string))
