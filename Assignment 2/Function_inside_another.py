def temper(cel):
    def to_fa(c):
        return (c * 9/5) + 32
    print("Fahrenheit =", to_fa(cel))

temper(30)