class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = "/"

        splited_path = [i for i in path.split('/') if i!='' and i!='.']

        stack = []

        for i in splited_path:
            if i=="..":
                if stack:
                    stack.pop()
                continue
            
            stack.append(i)


        return "/" + "/".join(stack)