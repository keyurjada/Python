with open("source.txt", "r") as src:
    data = src.read()

with open("destination.txt", "w") as dest:
    dest.write(data)

print("File copied successfully")