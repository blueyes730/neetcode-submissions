class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqindex will hold the num at jndex based in freq
        freqindex = [[] for i in range(len(nums)+1)]
        freqmap = {}

        for num in nums:
            freqmap[num] = freqmap.get(num, 0) + 1
        
        
        for j, v in freqmap.items():
            freqindex[v].append(j)
            
        
        freqindex.reverse()
        
        ret = []

        
        for l in freqindex:
            for i in l:
                if k == 0:
                    return ret
                else:
                    ret.append(i)
                    k-=1
        
        
        return ret
        