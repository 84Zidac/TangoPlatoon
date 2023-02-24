# def dietPlanPerformance(calories, k, lower, upper):
#         points = 0
#         if k == 1:
#             for each in calories:
#                 if each > upper:
#                     points += 1
#                 elif each < lower:
#                     points -=1
#             return points
#         start_index = 0
#         end_index = k-1
#         while end_index < len(calories):
#             block = 0
#             for num in range(start_index, end_index):
#                 block = block + calories[num]
#             if block > upper:
#                 points += 1
#                 start_index = start_index + k
#                 end_index = end_index + k
#             elif block < lower:
#                 points -= 1
#                 start_index = start_index + k
#                 end_index = end_index + k
#             else:
#                 start_index = start_index + k
#                 end_index = end_index + k
#         return points
# print(dietPlanPerformance([3,2], 2, 0, 1))


# def twoSum(nums, target):
#     checked = {}
#     i = 0
#     while target - nums[i] not in checked:
#         checked[nums[i]] = i
#         i += 1

#     return [checked[target - nums[i]], i]


        
# print(twoSum([2,7,11,15], 26) == [2,3])



# def findMedianSortedArrays(nums1, nums2):
#     i = 0
#     j = 0
#     while i < len(nums2):
#         if j == len(nums1) -1:
#             nums1.append(nums2[j])
#         print(nums1, nums2)
#         if nums2[i] < nums1[j]:
#             nums1.insert(j, nums2[i])
#             i+= 1
#         else:
#             j += 1
#     return nums1



# print(findMedianSortedArrays([1,2], [3,4]))


def decode(encoded, first):
    n = len(encoded) + 1
    arr = [0] * n
    arr[0] = first
    
    for i in range(1, n):
        arr[i] = encoded[i-1] ^ arr[i-1]
        
    return arr


print(decode([6], 1))







