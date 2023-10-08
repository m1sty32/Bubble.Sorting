def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

random_list = [5, 6, 8, 10, 9, 3, 1, 2, 0, 4]

bubble_sort(random_list)
print(random_list)

