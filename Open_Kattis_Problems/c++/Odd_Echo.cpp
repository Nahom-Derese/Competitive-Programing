#include<bits/stdc++.h>
using namespace std;

int main(){
    int x;
    string y;
    vector<string> m;
    cin >> x;

    for (short i = 1; i < x+1; i++)
    {
        cin >> y;
        if (i%2 != 0)
            m.push_back(y);
    }

    for (auto x:m)
        cout << x << endl;
    
    
    return 0;
}