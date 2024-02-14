import re



class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        binary = str(bin(n))
        count = 0

        def give_me_1000(m):
            regEx = r'1[0]*'
            global count
            if re.match(reg, m):
	            return m
            
            if m == '0':
                count+=1
                return '1'

            if m[0] == '0':
                count+=1
                return give_me_0(m[1:])
            
            elif m[0] == '1':
                count
                return give_me_1000(m[1:])
            
        def give_me_0(m):
            regEx = r'0+'
            global count
            if re.match(reg, m):
	            return m
            
            if m == '1':
                count+=1
                return '0'

            if m == '0':
                count+=1
                return '1'

            if m[0] == '0':
                return give_me_0(m[1:])
            
            elif m[0] == '1':
                return give_me_1000(m[1:])

                
        for i in range(len(binary)):
            if binary[i] == '1':
                binary = give_me_1000(binary[i+1:])                
            if binary[i] == '0':
                binary = give_me_0(binary)