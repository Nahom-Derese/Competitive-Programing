#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    
    while(t--){
        int n;
        cin >> n;
        map<int,int> m;
        int arr[n];

        int ans = -1;

        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            if (m.find(arr[i]) == m.end()) {
                m[arr[i]] = 1;
            } else {
                m[arr[i]]++;
                if (m[arr[i]] == 3)
                {
                    ans = arr[i];
                }
            }
        }

        cout << ans << endl;
        
        
    }

}