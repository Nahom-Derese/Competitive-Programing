#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T, n, p = 0, n1;
    string In, In2;
    cin >> T;
    int Ans[T];
    for (int i = 0; i < T; i++)
    {
        p = 0;
        cin >> n;
        int L[n] = {0};
        for (int j = 0; j < n; j++)
        {
            cin >> In;
            if (In == "LEFT")
            {
                p--;
                L[j] = -1;
            }
            if (In == "RIGHT")
            {
                p++;
                L[j] = 1;
            }
            if (In == "SAME")
            {
                cin >> In >> n1;
                if (L[n1 - 1] == 1)
                {
                    p++;
                    L[j] = 1;
                }
                if (L[n1 - 1] == -1)
                {
                    p--;
                    L[j] = -1;
                }
            }
        }

        Ans[i] = p;
    }

    for (int i = 0; i < T; i++)
    {
        cout << Ans[i] << endl;
    }
    return 0;
}