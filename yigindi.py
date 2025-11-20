# 10 ga teng
# nums = [2, 4, 5, 6, 8, 9]
#
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i]+nums[j] == 10:
#             print(nums[i],"+",nums[j])


# onga_teng = nums[2+8]
# for x in nums:
#     if x == onga_teng:
#         onga_teng = x
#
# print(onga_teng)

# sonlar = [1, 2, 5, 6]
#
# total = 0
#
# for i in sonlar:
#     total += i
# print(total)

nums = [3, 2, 1, 5, 6, 4]
k = 0

sorted_nums = sorted(nums, reverse=True)  # kamayishiga qarab tartiblash
print(f"The {k}th largest element is:", sorted_nums[k - 1] if k > 0 else None)





