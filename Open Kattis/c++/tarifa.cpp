#include<bits/stdc++.h>
using namespace std;

int main(){
    int x,y,z,ans;
    cin >> x >> y;
    ans = x;
    for (short i = 0; i < y; i++)
    {
        cin >> z;
        ans += x-z;
    }
    
    cout << ans << endl;
    return 0;
    }