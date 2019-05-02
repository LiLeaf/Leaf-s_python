'''1.Two Sum:
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target. You may assume that
    each input would have exactly one solution, and you may not use the same element twice.
    Example: Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].'''
def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            a=nums[i]
            for j in range(i+1,len(nums)):
                b=nums[j]
                if a+b==target:
                    return [i,j]

'''7. Reverse Integer:
    Given a 32-bit signed integer, reverse digits of an integer.
    Example:Input: 123    Output: 321
                Input: -123     Output: -321
                Input: 120       Output: 21'''
def reverse(self, x: int) -> int:
        rev=0
        intmax=2**31-1
        intmin=-2**31
        rev=int(str(abs(x))[::-1])
        rev=rev if x>0 else rev*(-1)
        return rev if intmin < rev < intmax else 0

'''9. Palindrome Number:
    Determine whether an integer is a palindrome. An integer is a palindrome
    when it reads the same backward as forward.
    Example:Input: 121     Output: true
                  Input: -121    Output: false
                  Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
                  Therefore it is not a palindrome.
                  Input: 10       Output: false
                  Explanation: Reads 01 from right to left. Therefore it is not a palindrome.'''
def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            if x==int(str(x)[::-1]):
                return True
            else:
                return False

'''14. Longest Common Prefix:
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    Example:Input: ["flower","flow","flight"]      Output: "fl"
                  Input: ["dog","racecar","car"]          Output: ""
                  Explanation: There is no common prefix among the input strings.'''
def longestCommonPrefix_1(self, strs: List[str]) -> str:
        result = []
        for e in ({*x} for x in zip(*strs)):
            if len(e) > 1:
                break
            result.append(e.pop())
        return ''.join(result)
def longestCommonPrefix_2(self, strs: List[str]) -> str:
    if len(strs) < 1:
        return ''
    prefix = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[ :len(prefix) - 1]
            if len(prefix) == 0:
                return ''
    return prefix
