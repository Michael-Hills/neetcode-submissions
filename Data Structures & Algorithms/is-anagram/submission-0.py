class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterDictS = dict()
        letterDictT = dict()

        for i in s:
            if i in letterDictS.keys():
                letterDictS[i] += 1
            else:
                letterDictS[i] = 1

        for i in t:
            if i in letterDictT.keys():
                letterDictT[i] += 1
            else:
                letterDictT[i] = 1
        

        if letterDictS == letterDictT:
            return True
        
        return False