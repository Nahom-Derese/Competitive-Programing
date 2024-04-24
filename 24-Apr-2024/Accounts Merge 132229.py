# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        size = {}
        names = {}

        for account in accounts:
            for i in range(1, len(account)):
                names[account[i]] = account[0]
                email = account[i]
                size[email] = 1
                parent[email] = email
        
        def find(x):
            if x == parent[x]:
                return x
            x = find(parent[x])
            return x
        
        def union(x,y):
            par_x = find(x)
            par_y = find(y)
            
            if size[par_x] > size[par_y]:
                parent[par_y] = par_x
                size[par_x]+=size[par_y]
            else:
                parent[par_x] = par_y
                size[par_y]+=size[par_x]

        for account in accounts:
            for i in range(2, len(account)):
                union(account[i-1], account[i])
       
        ans = defaultdict(set)
        for account in accounts:
            for i in range(1, len(account)):
                ans[find(account[i])].add(account[i])

        final_ans = []
        for key, value in ans.items():
            temp = [names[key]]
            value = list(value)
            value.sort()
            temp.extend(value)
            final_ans.append(temp)
        return final_ans
        