class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        stack = [] # index

        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                stack.append(i)
        print(stack)
        while stack:
            i = stack.pop()
            print(f"i: {i}")
            index = i
            g = 0
            count = 0
            while(True):
                if count == len(gas): return i
                else:
                    g += gas[index] - cost[index]
                    print(f"g += {gas[index]} - {cost[index]} = {g}")
                    if g < 0: break
                    index = (index + 1) % len(gas)
                    count += 1

        
        return -1
            
            