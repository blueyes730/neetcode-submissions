class Solution:
    def twoSum(numbers: List[int], target: int, solutions: List[List[int]]) -> List[int]:
        l, r = 1, len(numbers) - 1
        target *= -1
        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                thing = [-1*target, numbers[l], numbers[r]]
                if thing not in solutions:
                    solutions.append(thing)
                l += 1
                while numbers[l] == numbers[l-1] and l < r:
                    l+=1
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        solutions = []
        for i, a in enumerate(nums):
            if i < 0 and a != nums[i-1]: # take care of duplicates
                continue
            Solution.twoSum(nums[i:], a, solutions)
        
        return solutions




            
        

         
        