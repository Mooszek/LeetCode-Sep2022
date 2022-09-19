class Solution:
    def __init__(self,strs):
        self.strs = strs

    def longestCommonPrefix(strs):
        strs.sort()
        firstword = list(strs[0])
        lastword = list(strs[len(strs)-1])
        result = []
        for i, char in enumerate(firstword):
            if char == lastword[i]:
                result.append(char)
            else:
                break
            
        return ''.join(result)

lista = ["dog","racecar","car"]  #example

wynik = Solution.longestCommonPrefix(lista)
print(wynik)