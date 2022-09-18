class Solution:
    def __init__(self,x):
        self.x = x

    def isPalindrome(x):
        y = str(x)
        y= y[::-1]
        print(y)
        if y==str(x):
            return True
        else:
            return False

x= Solution.isPalindrome(121)
print(x)