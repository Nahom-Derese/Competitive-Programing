from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        reversedNums = list(reversed(nums))
        prefixSum = [0]
        sufixSum = [0]
        secret = []
        secretReversed = []
        answer = []
        
        for i in nums[:-1]:
            prefixSum.append( prefixSum[-1] + i)

        for i in nums[::-1][:-1]:
            sufixSum.append( sufixSum[-1] + i)

        for i in range(len(nums)):
            secret.append(i*nums[i])

        for i in range(len(nums)):
            secretReversed.append(i*reversedNums[i])

        sufixSum.reverse()
        secretReversed.reverse()

        for i in range(len(nums)):
            answer.append(secret[i] - prefixSum[i] + sufixSum[i] - secretReversed[i])

        return answer


