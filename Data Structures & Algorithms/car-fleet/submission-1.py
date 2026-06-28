class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combine = [(p,s) for p,s in zip(position, speed)]

        combine.sort(reverse=True
        )
        stack = []
        for p,s in combine:
            t = (target-p) / s
            stack.append(t)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)