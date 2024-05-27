# https://leetcode.com/problems/palindrome-number/description/

# Method 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        a=x
        while(x>0):
            rem= x%10
            rev=rev*10+rem
            x//=10

        if a==rev:
            return True
        else:
            return False
        

        