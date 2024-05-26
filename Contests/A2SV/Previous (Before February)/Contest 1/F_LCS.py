s1 = input()
s2 = input()

def dp(n: int, m: int) -> int:
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


    index = dp[n][m]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = n
    j = m
    while i > 0 and j > 0:

        if s1[i-1] == s2[j-1]:
            lcs_algo[index-1] = s1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_algo)


print(dp(len(s1), len(s2)))