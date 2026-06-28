import queue

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures) 
        stack = [] # index, val
        for i, temp in enumerate(temperatures):
            
            # while either the stack isn't empty or the top of the stack is less than the current item
            while stack and stack[-1][1] < temp:
                item_idx, item_temp = stack.pop()
                ret[item_idx] = i - item_idx
            stack.append((i, temp))
        
        return ret



            


