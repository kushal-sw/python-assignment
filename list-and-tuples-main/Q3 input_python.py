nums = [1, 2, 2, 3, 3, 3]

count = {}

for n in nums:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

print(count)
