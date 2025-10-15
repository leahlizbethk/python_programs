# Given a list of integers, write a function that returns 
# the largest sum of non-adjacent numbers. 
# Given a list of integers, write a function that returns
# the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since 
# we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, 
# For example, [2, 4, 6, 2, 5] should return 13, since
# we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
# since we pick 5 and 5.

def largest_non_adjacent_sum(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return max(0, nums[0])
    
    # Initialize the first two sums
    incl = max(0, nums[0])  # max sum including the first element
    excl = 0                 # max sum excluding the first element
    
    for num in nums[1:]:
        # Temporarily store the new max excluding current
        new_excl = max(incl, excl)
        
        # Update incl to include current num
        incl = excl + num
        # Update excl to the previous maximum
        excl = new_excl
    
    # The answer is the max of incl and excl
    return max(incl, excl)

# Main program
if __name__ == "__main__":
    # Input: list of integers separated by space
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    result = largest_non_adjacent_sum(nums)
    print("Largest sum of non-adjacent numbers:", result)
