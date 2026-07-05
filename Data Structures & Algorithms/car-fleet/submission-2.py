class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0 or len(speed) == 0: return 0
        

        motion = sorted([(p,s) for p, s in zip(position, speed)], key = lambda x : x[0])
        print(motion)
        
        prev = (target - motion[-1][0]) / motion[-1][1]
        fleets = 1

        for i in range(len(motion) - 2, -1, -1):
            curr = (target - motion[i][0]) / motion[i][1]
            if curr > prev:
                fleets += 1
                prev = curr
        
        return fleets

