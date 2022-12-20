x = ['ab','b','ce','de','e']

# Working
print(list(map(len,x)))

# Not Working
print(list(map(len(x),x)))