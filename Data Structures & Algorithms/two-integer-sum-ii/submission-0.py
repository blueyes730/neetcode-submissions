class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, (len(numbers)-1)
        while s < e:
            summ = numbers[s]+numbers[e]
            if summ > target:
                e-=1
            elif summ < target:
                s+=1
            else:
                return [s+1,e+1]
        return [s+1,e+1]