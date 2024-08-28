class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m , n = [len(mat), len(mat[0])]

        e = [(0, i) for i in range(n)] + [(i, n-1) for i in range(1,m)]

        def diagonal(t):
            r, c = t
            p = []
            while r < m and c > -1:
                p.append(mat[r][c])
                r+=1
                c-=1
            return p

        ans = []
        for i in range(len(e)):
            u = diagonal(e[i])
            print(u)
            if i%2==0:
                ans.extend(reversed(u))
            else:
                ans.extend(u)

        return ans