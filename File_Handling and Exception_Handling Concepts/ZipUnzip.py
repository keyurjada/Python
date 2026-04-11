import zipfile

# Zip file
with zipfile.ZipFile("files.zip", "w") as z:
    z.write("sample.txt")

print("File zipped")

# Unzip file
with zipfile.ZipFile("files.zip", "r") as z:
    z.extractall("output")

print("File unzipped")