from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range((len(nums) + 1))]
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        for num, count in counter.items():
            freq[count].append(num)
        
        ret = []
        # print(freq)
        for i in range(len(freq) - 1, -1, -1):
            # print(i)
            # print(freq[i])
            for j in freq[i]:
                if len(ret) == k:
                    return ret
                
                ret.append(j)

        return ret

        



        