class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val1={}
        val2={}
        for i in s:
            val1[i]=val1.get(i,0)+1
        for j in t:
            val2[j]=val2.get(j,0)+1
        return val1==val2
            



        