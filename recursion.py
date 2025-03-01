"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Alberto Cabrera and <FULL NAME>, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1:AC82885
UT EID 2:
"""


# TODO: Modify this function. You may delete this comment when you are done.
def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start == len(nums):
        return False
    if group_sum(start+1,nums,target-nums[start]):
        return True
    elif group_sum(start+1,nums,target):
        return True
    return False
    


# TODO: Modify this function. You may delete this comment when you are done.
def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start == len(nums):
        return False
    if group_sum_6(start+1,nums,target-nums[start]) and nums[start] == 6:
        return True
    elif group_sum_6(start+1,nums,target):
        return True
    return False


# TODO: Modify this function. You may delete this comment when you are done.
def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start == len(nums):
        return False
    if group_no_adj(start+2,nums,target-nums[start]):
        return True
    elif group_no_adj(start+1,nums,target):
        return True
    return False


# TODO: Modify this function. You may delete this comment when you are done.
def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start == len(nums):
        return False
    if group_sum_6(start+2,nums,target-nums[start]) and nums[start] == 6:
        return True
    elif group_sum_6(start+1,nums,target):
        return True
    return False


# TODO: Modify this function. You may delete this comment when you are done.
def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start == len(nums):
        return False
    clump = nums[start]
    right_index = start+1
    for i in range(start,len(nums)-1):
        if nums[i]==nums[start]:
            clump += nums[i]
            right_index += 1
    if group_sum_clump(right_index,nums,target-clump):
        return True
    if group_sum_clump(right_index,nums,target):
        return True
    return False



# TODO: Modify this function
def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    if sum(nums) %2 == 1:
        return False
    target = sum(nums)/2
    def helper_func(start, nums, target):
        if target == 0:
            return True
        if start >= len(nums):
            return False
        if helper_func(start+1,nums,target-nums[start]):
            return True
        if helper_func(start+1,nums,target):
            return True
        return False #rahhh i love copy and pasting group_sum 19283712 times
    return helper_func(0, nums, target)



# TODO: Modify this function. You may delete this comment when you are done.
def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    #wtf is this
    def helper_func(start, mult, odd):
        if start == len(nums):
            return mult % 10 == 0 and odd % 2 == 1
        if helper_func(start+1,mult + nums[start],odd):
            return True
        if helper_func(start+1,mult,odd + nums[start]):
            return True
        return False
    return helper_func(0, 0, 0)

# TODO: Modify this function. You may delete this comment when you are done.
def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def helper_func(start,mult5,mult3):
        if start == len(nums):
            return mult5==mult3
        if nums[start] % 5 == 0:
            return helper_func(start+1,mult5+nums[start],mult3)
        if nums[start] % 3 == 0:
            return helper_func(start+1,mult5,mult3+nums[start])
        if helper_func(start+1,mult5+nums[start],mult3):
            return True
        if helper_func(start+1,mult5,mult3+nums[start]):
            return True
        return False
    return helper_func(0,0,0)
