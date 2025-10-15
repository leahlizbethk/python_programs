# find the lowest
# positive integer that does not exist in the array. The array can
# contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. 
# For example, the input [3, 4, -1, 1] should give 2.
# The input [1, 2, 0] should give 3.




def first_missing_positive(nums):
    nums = set(nums)  # remove duplicates and allow O(1) lookups
    i = 1  # start checking from the smallest positive number
    while i in nums:
        i += 1
    return i


#main
nums_input = input("Enter numbers separated by spaces: ")
nums = list(map(int, nums_input.split()))

result = first_missing_positive(nums)

print("The smallest missing positive integer is:", result)
