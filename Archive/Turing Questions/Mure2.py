def solution(r):
    ans = []
    for i in r:
        if r.count(i) == i:
            ans.append(i)
    
    if len(ans) == 0:
        return -1
    else:
        return(max(ans))



   
    
print(solution([2,2,3,4]))
print(solution([1,2,2,3,3,3]))
print(solution([2,2,2,3,3]))
print(solution([5]))