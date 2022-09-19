class Solution:
    def __init__(self,s):
        self.s = s

    def convertToNumber(letter):
        romanNumbers ={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        return int(romanNumbers[letter])
    
    def romanToInt(s):
        s = s[::-1]
        number = 0
        lastDigit = 0
        while len(s) > 0:
            digit = Solution.convertToNumber(s[0])
            if digit >= lastDigit:
                number += digit
                lastDigit = digit
            else:
                number -= digit
            s = s[slice(1,len(s))]

        return number


s = Solution.romanToInt("III")

print(s)