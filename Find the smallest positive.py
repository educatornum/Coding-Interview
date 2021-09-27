# Find the smallest positive number missing from an unsorted
# Array dotor baihgui hamgiin eyreg elemtiig ol

#  Input:  {2, 3, 7, 6, 8, -1, -10, 15}
#  Output: 1

#  Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
#  Output: 4

#  Input: {1, 1, 0, -1, -2}
#  Output: 2

import unittest
def solution_a(a):
    B = set(sorted(a))
    m = 1
    for x in B:
        if x == m:
            m+=1
    return m
arr = [1, 3, 6, 4, 1, 2]
print(solution_a(a=arr))

# class TestSolutionA(unittest.TestCase):
#     def test_case0(self):
#       input_list = [1, 3, 6, 4, 1, 2]
#       val = solution_a(input_list)
#       self.assertEqual(val, 5)

#     def test_case1(self):
#       input_list = [1, 2, 3]
#       val = solution_a(input_list)
#       self.assertEqual(val, 4)
# if __name__ == '__main__':
#     unittest.main()
