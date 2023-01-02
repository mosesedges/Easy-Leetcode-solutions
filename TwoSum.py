'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

def two_sum(nums=list[int], target=int()): 
    hashmap = {} # create an empty dictionary to store each number and it value
    for index, number in enumerate(nums): # get the list index(positions of the each number) and the number itself from the num(list)
        diff = target - number # subtract the each number from the target and save the result in diff
        if diff in hashmap: #check if the diff is already in the hashmap(dictionary)
            return [hashmap[diff], index] # if the difference is in the dictionary return a list of the index of the diff and the index of the number itself 
        hashmap[number] =  index # if the diff is not in the hashmap add the number to the hashmap as a key and it index as it value
    