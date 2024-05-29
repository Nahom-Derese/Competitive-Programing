# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, d1: int, d2: int, cnt1: int, cnt2: int) -> int:
        def gcd(a,b):
            if a==0:
                return b
            if b==0:
                return a
            if a==b:
                return a
            if a>b:
                return gcd(a-b,b)
            return gcd(a,b-a)

        lcm=(d1*d2)//gcd(d1,d2)
        l=1
        r=10**15
        ans=r
        while l<=r:
            mid=(l+r)//2
            if d1==d2:
                if cnt1+cnt2 <= mid-(mid//d1):
                    ans=mid
                    r=mid-1
                else:
                    l=mid+1
            else:
                common=mid//lcm
                c1=(mid//d2)-common
                c2=(mid//d1)-common
                temp1=cnt1-min(cnt1,c1)
                temp2=cnt2-min(cnt2,c2)
                if temp1+temp2<=mid-(c1+c2+common):
                    ans=mid
                    r=mid-1
                else:
                    l=mid+1
        return ans