# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Test File:
# from whiteboard import *
# # change whiteboard to python file name, you can change * to function name
# import unittest

# class CalculatorTest(unittest.TestCase):

#     def test_check_lucky(self):
#         result1 = check_lucky([2,2,3,4])
#         self.assertEqual(result1, 2)
#         result2 = check_lucky( [1,2,2,3,3,3])
#         self.assertEqual(result2, 3)
        
#     def test_no_luck(self):
#         result = check_lucky([2,2,2,3,3])
#         self.assertEqual(result, -1)

# unittest.main()


def lucky_number(arr):
    lucky_num = -1
    for num in arr:
        if arr.count(num) == num:
            max_freq = num
            if max_freq > lucky_num:
                lucky_num = max_freq
    return lucky_num

def check_lucky(alist):
    try:
        return max(num for num in alist if num == alist.count(num))
    except:
        return -1

print(check_lucky([33,4,6,4,10]))


def check_lucky_effecient(alist):
    hash_map,output = {}, []
    for num in alist:
        hash_map[num] = hash_map.get(num,0)+1
        """
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1
        """

    for num, num_count in hash_map.items():
        if num == num_count:
            output.append(num)
    #output = [num for num, num_count in hash_map.items() if num == count]
    return max(output) if output else -1

print(check_lucky_effecient([1,1,2,3]))
