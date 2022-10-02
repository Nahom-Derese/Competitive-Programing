#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<float> a;
    int n,m;
    cin >> n;
    for (short i = 0; i < n; i++)
    {
        cin >> m;
        for (short j = 0; j < m; j++)
        {   
            int w[m + 1];
            cin >> w[j];
            if(j==0)
                w[m] = 0;
            w[m] += w[j];
            if (j==m-1)
            {
                float ave = w[m] / m;
                float r = 0.000;
                for (short k = 0; k < m; k++)
                    r = ave < w[k] ? ++r : r;
                a.push_back((r / m) * 100.000);
            }
        }
        
    }
    
    for (auto p: a)
        printf("%.3f%\n", p);
    return 0;
}