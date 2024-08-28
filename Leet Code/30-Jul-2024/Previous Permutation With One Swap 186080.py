# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        last_number = arr[n-1] 
        res_pos, res_pos_2 = -1, -1
        res_value, res_value_2 = None, None

        for i in range(n-1): 
            if arr[n-i-2] > arr[n-i-1]:
                res_pos = n-i-2
                res_value = arr[n-i-2]
                break
        
        if res_pos == -1:
            return arr

        for i in range(res_pos+1,n): 
            if i == n-1 or arr[i+1] > res_value:
                res_pos_2 = i
                res_value_2 = arr[i]
                break

        if res_value == res_value_2:
            res_pos_2 = res_pos+1
            res_value_2 = arr[res_pos+1]

        if res_pos != -1 and res_pos_2 != -1:
            arr[res_pos] = res_value_2
            arr[res_pos_2] = res_value

        return arr