with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

    words = content.split()
    print("Total Words:", len(words))