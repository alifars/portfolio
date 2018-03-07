arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1]
k = 10
num = 6
# assert_equal(sol([1, 2, 3, 1], 3), 1)
# assert_equal(sol([1, 3, 2, 2], 4), 2)

remain_dict = {}
for val in arr:
    remain_dict[k - val] = val

print(remain_dict)

result = set()
another_dict = {}
for val in arr:
    if val in remain_dict:
        val,remain_dict[val]

print(another_dict)
