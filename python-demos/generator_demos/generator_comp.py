

nums = [1,2,3,4,5]

# double_nums = []
# for num in nums:
#     double_nums.append(num * 2)

# double_nums = map(lambda x: x * 2, nums)

# double_nums = [ x * 2 for x in nums ]

double_nums = ( x * 2 for x in nums )

print(nums)
print(list(double_nums))
