class Outer:
    def __init__(self):
        self.msg = "Outer Class"

    class Inner:
        def display(self):
            print("Inner Class Method")

o = Outer()
i = Outer.Inner()

print(o.msg)
i.display()