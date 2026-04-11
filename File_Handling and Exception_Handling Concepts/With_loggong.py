import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print("Result:", a / b)

except Exception as e:
    logging.error("Error occurred: %s", e)
    print("Exception occurred. Check log file.")