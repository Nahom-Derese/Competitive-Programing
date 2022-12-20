def listSkills(val, list=[]):
    list.append(val)
    return list

list1 = listSkills('Node JS')
list2 = listSkills('JAVA', [])
list3 = listSkills('React JS')

print("%s" % list1)
print("%s" % list2)
print("%s" % list3)