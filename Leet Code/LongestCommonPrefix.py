


class Solution:

    def longestCommonPrefix(self, strs):

        maxLength = 0
        for i in strs:

            maxLength = max(len(i), maxLength)


        minimum = maxLength

        for j in strs[1:]:
            count = 0
            try:
                while j[count] == strs[0][count]:
                    count+=1
            except:
                pass
            minimum = min(minimum, count)

        print(strs[0][:minimum])



Solution().longestCommonPrefix(["flower","flow","flight"])
Solution().longestCommonPrefix(["dog","racecar","car"])
Solution().longestCommonPrefix(["",""])