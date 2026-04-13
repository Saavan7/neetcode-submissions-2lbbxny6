from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fin=list()
        vals=defaultdict(list)
        for i in strs:
            letters=[0]*26
            for j in i:
                letters[ord(j)-ord('a')]+=1
            vals[tuple(letters)].append(i)
        for k in vals.values():
            fin.append(k)
        return fin
            
        
        

        

        