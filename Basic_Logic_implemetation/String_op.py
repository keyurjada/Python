s = input("Enter string: ")

vowels = "aeiouAEIOU"
count = 0
for i in s:
    if i in vowels:
        count += 1
print("Vowels =", count)

length = 0
for i in s:
    length += 1
print("Length =", length)

rev = s[::-1]
print("Reverse =", rev)

old = input("Enter word to find: ")
new = input("Enter replacement: ")
print("Result =", s.replace(old,new))

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")