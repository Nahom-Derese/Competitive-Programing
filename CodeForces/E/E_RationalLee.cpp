#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;

    cin >> t;

    while(t--){
        long long n, m;
        long long  c = 0;
        cin >> n >> m;

        vector<long long> a(n);
        vector<long long> b(m);

        for(long long i = 0; i < n; i++){
            cin >> a[i];
        }

        for(long long i = 0; i < m; i++){
            cin >> b[i];
            if(b[i] == 1){
                c++;
            }
        }

        sort(a.begin(), a.end());
        sort(b.rbegin(), b.rend());

        long long ans = 0;
        long long j = 0;

        for (long long i = n-m; i < n; i++) {
            ans += a[i];
        }

        for (long long i = n-c; i < n; i++) {
            ans += a[i];
        }

        long long i = 0;

        while (i < n-m && j < m-c) {
            ans += a[i];
            i+=b[j]-1;

            j++;
        }

        cout << ans << endl;
    }

    return 0;
}