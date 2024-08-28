class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens = 0
        fives = 0
        tewenies = 0

        for i in bills:
            if i == 5:
                fives+=1
            elif i == 10 and fives > 0:
                tens+=1
                fives-=1
            elif i == 20 and tens > 0 and fives > 0:
                tens-=1
                fives-=1
                tewenies+=1
            elif i == 20 and tens == 0 and fives > 2:
                fives-=3
                tewenies+=1
            else:
                return False
        return True

                