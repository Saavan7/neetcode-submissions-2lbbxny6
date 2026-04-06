class Solution(object):
    def topKFrequent(self, nums, k):
        vals={}
        vals2=[]
        fin=set()
        for i in nums:
            vals[i]=vals.get(i,0)+1
        for i in vals.values():
            vals2.append(i)
        vals2.sort(reverse=True)
        for i in range(0,k):
            for x,y in vals.items():
                if y==vals2[i]:
                    fin.add(x)
        return list(fin)