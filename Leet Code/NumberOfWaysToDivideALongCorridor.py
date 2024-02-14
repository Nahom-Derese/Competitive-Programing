from functools import cache, reduce
from operator import mul

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        each_compartment = []
        number_of_s=corridor.count('S')
        l_p = 0
        r_p = 0
        i = 0
        ans=1

        if number_of_s < 2:
            return 0

        elif number_of_s < 4:
            return 1

        @cache
        def howManyWays(subArray:str) -> int:
            number_of_s=subArray.count('S')
            if number_of_s < 2:
                return 0
            elif number_of_s == 2:
                return 1
            else:
                l_p = 0
                r_p = len(subArray)-1
                for i in range(2):
                    while subArray[l_p] != 'S':
                        l_p+=1
                    while subArray[r_p] != 'S':
                        r_p-=1
                    l_p+=1
                    r_p-=1
                return r_p-l_p+2
        
        while r_p < len(corridor) and i < 4:
            if corridor[r_p] == 'S':
                i+=1
            r_p+=1

        each_compartment.append(howManyWays(corridor[l_p:r_p]))

        while r_p < len(corridor):
            i = 0
            j = 0

            while r_p < len(corridor) and i < 2:
                if corridor[r_p] == 'S':
                    i+=1
                r_p+=1
            
            while l_p < len(corridor) and j < 3:
                if corridor[l_p] == 'S':
                    j+=1
                l_p+=1
            l_p-=1

            each_compartment.append(howManyWays(corridor[l_p:r_p]))

        ans = reduce(mul, each_compartment)
        
        return ans % MOD



# print(Solution().numberOfWays("PPSSPSSPPPSPSSSPSSPPSPS"))
# print(Solution().numberOfWays("SSSPPPSPPSPSSSSSSPPPSPP"))
# print(Solution().numberOfWays("PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS"))
# print(Solution().numberOfWays("SSPPSPS"))
# print(Solution().numberOfWays("PPSPSP"))
# print(Solution().numberOfWays("S"))