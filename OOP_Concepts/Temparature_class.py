class Temperature:
    def convertFahrenheit(self, c):
        return (c * 9/5) + 32

    def convertCelsius(self, f):
        return (f - 32) * 5/9

t = Temperature()

print("Celsius to Fahrenheit:", t.convertFahrenheit(25))
print("Fahrenheit to Celsius:", t.convertCelsius(77))