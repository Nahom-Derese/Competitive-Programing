#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, counter=0, ans=0;
    char t;
    string y;
    map<char,int> w;
    while (true)
    {
        cin >> n;
        if (n == -1)
           break;
        cin >> t >> y;
        if (y=="right")
        {
            counter++;
            ans+=n+w[t];
        }
        else if(y=="wrong")
            w[t] += 20;
    }
    
    cout << counter << " " << ans << endl;

    return 0;
}