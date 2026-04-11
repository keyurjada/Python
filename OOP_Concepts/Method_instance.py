class Example:
    count = 0   # class variable

    def __init__(self):
        Example.count += 1

    def show(self):  # instance method
        print("Instance Method Called")

    @classmethod
    def show_count(cls):  # class method
        print("Total Objects:", cls.count)

obj1 = Example()
obj2 = Example()

obj1.show()
Example.show_count()