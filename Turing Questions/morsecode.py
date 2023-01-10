def morsecode(code: str):
    lst = []
    for i in range(len(code) - 1):
        # replace("This", "With This", only the 1st occurence)
        lst.append(code[:i] + code[i:].replace("..","--",1))
    return lst

print(morsecode("....."))