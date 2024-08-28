# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        indegree = defaultdict(lambda: float("inf"))

        for supply in supplies:
            indegree[supply]=0

        for i in range(len(recipes)):
            recipe = recipes[i]
            ingredient = ingredients[i]
            
            for j in ingredient:
                graph[j].append(recipe)
                if indegree[recipe] == float("inf"):
                    indegree[recipe]=1
                else:
                    indegree[recipe]+=1


        def topsort(multisource):
            res = []
            queue = deque(multisource)

            while queue:
                x = queue.popleft()
                
                if x in recipes:
                    res.append(x)

                for node in graph[x]:
                    indegree[node]-=1
                    if indegree[node]:
                        continue
                    queue.append(node)
                    
            return res

        start = [ingredient for ingredient in supplies]

        return topsort(start)