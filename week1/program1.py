
# Given a list of numbers and a number k, return wheather any two
# numberrs from the list add up to k.


#logic
def has_pair_with_sum(nums, k):
    seen = set()  # keep track of numbers we've already seen
    for num in nums:
        complement = k - num  # the number we need to reach k
        if complement in seen:  # check if that number was already seen
            return True  # found a pair
        seen.add(num)  # remember the current number for future checks
    return False  # no pair found after checking all numbers


#main
nums_input = input("Enter numbers separated by spaces: ")
nums = list(map(int, nums_input.split()))  
k = int(input("Enter the target sum (k): "))
result = has_pair_with_sum(nums, k)


if result:
    print("Yes, there are two numbers that add up to", k)
else:
    print("No, there are no two numbers that add up to", k)
