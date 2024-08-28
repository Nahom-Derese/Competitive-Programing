#include <bits/stdc++.h>

using namespace std;

int T, n, m, q;

bool dfs(int start, vector<vector<int>> AL, int end);

int main()
{
    int a, b;
    cin >> T;
    vector<vector<int>> Ans;
    for (int i = 0; i < T; i++)
    {
        cin >> n >> m >> q;
        bool AM[n][n] = {false};
        vector<vector<int>> AL(n);
        vector<int> ans;
        for (int j = 0; j < n; j++)
        {
            for (int e = 0; e < n; e++)
            {
                cin >> AM[j][e];
                if (AM[j][e])
                {
                    AL[j].push_back(e);
                    AL[e].push_back(j);
                }
            }
        }

        for (int k = 0; k < q; k++)
        {
            cin >> a >> b;
            if (dfs(a, AL, b))
                ans.push_back(1);
            else
                ans.push_back(0);
        }
        Ans.push_back(ans);
    }
    int k = 1;
    for (auto u : Ans)
    {
        cout << "Case" << k << endl;
        for (auto e : u)
        {
            cout << e << endl;
        }
        k++;
    }
    return 0;
}

bool dfs(int start, vector<vector<int>> AL, int end)
{
    stack<int> stack;
    stack.push(start);
    bool Visited[n] = {0};
    while (!stack.empty())
    {
        int temp = stack.top();
        Visited[temp] = 1;
        stack.pop();
        for (auto t : AL[temp])
        {
            if (!Visited[t])
                stack.push(t);
        }
    }
    if (Visited[end])
        return true;
    else
        return false;
}
