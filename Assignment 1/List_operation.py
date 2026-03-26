# Initial Lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("Initial list1:", list1)
print("Initial list2:", list2)
print("-" * 50)

# i. List Concatenation
list3 = list1 + list2
print("i. Concatenated List:", list3)

# ii. Remove list1[3]
list1.pop(3)
print("ii. After removing list1[3]:", list1)

# iii. Add 'Java' in list1
list1.append("Java")
print("iii. After adding 'Java':", list1)

# iv. Update list2 as list2[3] = 11
list2[3] = 11
print("iv. After updating list2[3] = 11:", list2)

# v. del list2[2]
del list2[2]
print("v. After deleting list2[2]:", list2)

# vi. Print message 4 times
print("vi. Printing message 4 times:")
for i in range(4):
    print("Welcome to Marwadi University")

# vii. Slicing operations
print("vii. Slicing Operations:")
print("list1[-2]:", list1[-2])
print("list2[1:3]:", list2[1:3])
print("list1[-1:-3]:", list1[-1:-3])

# viii. Length of list2
print("viii. Length of list2:", len(list2))

# ix. Maximum element in list1
print("ix. Maximum element in list1:", max(list1, key=str))

# x. Minimum element in list2
print("x. Minimum element in list2:", min(list2))

# xi. Append 100 to list2
list2.append(100)
print("xi. After appending 100 to list2:", list2)

# xii. Extend operation on list2
list2.extend([8, 9])
print("xii. After extending list2:", list2)

# xiv. Difference between pop() and remove()
demo_list = [10, 20, 30, 40]
print("xiv. POP vs REMOVE demonstration")
print("Original list:", demo_list)

demo_list.pop(2)   # removes element at index 2
print("After pop(2):", demo_list)

demo_list.remove(20)  # removes element with value 20
print("After remove(20):", demo_list)

# xv. Reverse list1
list1.reverse()
print("xv. After reversing list1:", list1)

# xvi. Sort list2 in descending order
list2.sort(reverse=True)
print("xvi. list2 in descending order:", list2)