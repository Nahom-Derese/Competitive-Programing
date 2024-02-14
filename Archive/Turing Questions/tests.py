class Circle:
    def draw(self):
        print(f"Inside Circle::draw()")
    def resize(self):
        print(f"Inside Circle::resize()")

a = Circle()

print(a.draw())