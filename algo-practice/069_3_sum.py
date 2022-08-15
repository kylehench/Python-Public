class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i, target in list(enumerate(nums))[:-1]:
            # if target == nums[i+1]:
                # continue
            j = i+1
            k = len(nums)-1
            while j != k:
                partial_sum = nums[j] + nums[k]
                if partial_sum < -target:
                    j += 1
                elif partial_sum > -target:
                    k -= 1
                    # while nums[k]==nums[k+1]:
                        # k -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # while nums[j]==nums[j-1]:
                        # j += 1
        triplets.sort()
        if len(triplets) > 0:
            res = [triplets[0]]
            prev = triplets[0]
            for i in range(1, len(triplets)):
                if triplets[i] != prev:
                    res.append(triplets[i])
                prev = triplets[i]
        else:
            res = []
        return res