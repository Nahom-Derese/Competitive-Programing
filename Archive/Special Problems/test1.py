class Developer(object):
    def __init__(self, skills):
        print("INIT")
        self.skills = skills

    def __str__(self):
        print("STR")
        return "Skills"
    
    def __add__(self, other):
        print("ADD")
        skills = self.skills + other.skills
        return Developer(skills)
    
A = Developer('Python')
B = Developer('Node JS')

print(A+B)