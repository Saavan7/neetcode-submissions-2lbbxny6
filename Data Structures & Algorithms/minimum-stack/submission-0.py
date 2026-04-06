class MinStack:

    def __init__(self):
        self.Minstack=[]

    def push(self, val: int) -> None:
        self.Minstack.append(val)

        

    def pop(self) -> None:
        self.Minstack.pop()
    

        

    def top(self) -> int:
        return self.Minstack[-1]
        

    def getMin(self) -> int:
        count=self.Minstack[0]
        for i in self.Minstack:
            count=min(i,count)
        return count
        