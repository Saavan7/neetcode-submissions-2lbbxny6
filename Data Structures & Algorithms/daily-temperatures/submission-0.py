class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days=[]
        for i in range(len(temperatures)):
            count=0
            for j in range(i+1,len(temperatures)):
                count+=1
                if temperatures[j]>temperatures[i]:
                    days.append(count)
                    break
            else:
                days.append(0)
        return days





        