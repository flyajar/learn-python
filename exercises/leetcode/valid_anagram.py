# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_list = []
        my_list[:0] = t
        for element in s:
            if element not in my_list:
                print('here')
                return False
            return True

solution = Solution()
print(solution.isAnagram('aacc', 'ccac'))
