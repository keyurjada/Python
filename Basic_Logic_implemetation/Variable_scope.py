x = 100
def function1():
    x = 50
    def function2():
        nonlocal x
        x = 25
        print("Value in function2:", x)
    function2()
    print("Value in function1:", x)
function1()
print("Global value of x:", x)