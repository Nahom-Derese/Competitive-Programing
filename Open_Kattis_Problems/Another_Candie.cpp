#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<bool> an;
     long long n,m,sum;
    cin >> n;
    for ( long long i = 0; i < n; i++)
    {
        sum = 0;
        cin >> m;
        long long l[m];
        for (long long j = 0; j < m; j++)
        {
            cin >> l[j];
            sum += l[j];
            if (j==m-1){
                if (sum % m == 0)
                    an.push_back(true);
                else
                    an.push_back(false);
                }
        }
        
    }


    for (int i = 0; i < n; i++){
        string ans = an[i] ? "YES" : "NO";
        cout << ans << endl;
    }
    
    
    return 0;
}