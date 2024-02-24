class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = [i[::-1] for i in image]
        for i in range(len(ans)):
            for j in range(len(ans)):
                    ans[i][j] = int(not bool(ans[i][j]))
        return ans