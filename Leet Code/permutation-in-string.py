class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)-1
        current_window = Counter(s2[:r])
        target_window = Counter(s1)

        if len(s1) > len(s2):
            return False

        while r < len(s2):
            current_window[s2[r]]+=1

            if target_window == current_window:
                return True

            current_window[s2[l]]-=1
            if not current_window[s2[l]]:
                del(current_window[s2[l]])
            r+=1
            l+=1

        return False