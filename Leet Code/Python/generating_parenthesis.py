import itertools


def check_parenthesis(g):
    stack = []
    
    for i in g:
        if i == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

def generate_permuation(a):
    
    b = ["(" if i % 2 == 0 else ")" for i in range((2 * a) - 2)]

    permutations = list(map(lambda e: "(" + ''.join(e) + ")", list(itertools.permutations( "".join(b) ))))

    # answer = []

    # count = 0
    # for i in permutations:
    #     if check_parenthesis(i):
    #         answer.append(i)

    # answer = list(set(answer))

    return permutations




    

# for i in generate_permuation(6):
#     print(i)
print(len(generate_permuation(5)))