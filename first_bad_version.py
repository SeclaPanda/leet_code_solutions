# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = n // 2
        if (isBadVersion(i) == True):
            while (isBadVersion(i) != False):
                i -= 1
            i += 1    
        else:
            while(isBadVersion(i) != True):
                i += 1
        return i


#below is official solution from leetcode. I wrote it, because my solution can't
#make an answer in time in big case.
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        rignt = n
        while (left < right):
            mid = left + (right - left) // 2
            if (isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1
        return left
'''