class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        

        def back(idx, current):
            # print(current)
            if idx == len(num):
                return len(current) > 2 and current[-1] == current[-2] + current[-3]

            for i in range(idx, len(num)):
                v = num[idx: i+1]
                if len(str(int(v))) == len(v):
                    val = int(v)
                    # print(val, idx)
                    if len(current) < 2 or current[-1] + current[-2] == val:
                        current.append(val)
                        if back(i+1, current):
                            return True
                        current.pop()
                    
    
        if len(num) > 2:
            return back(0, [])
        return False