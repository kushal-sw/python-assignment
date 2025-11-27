nums = [1, 2, 2, 3, 4, 4, 5]
new_list = []

for n in nums:
    if n not in new_list:
        new_list.append(n)

print("List without duplicates:", new_list)
