#include<bits/stdc++.h>
using namespace std;

int main(){
    int s,t,x,sum;
    cin >> s;
    vector<int> output;
    for (short i = 0; i < s; i++)
    {
        cin >> t;
        sum = 0;
        for (short j = 0; j < t; j++)
        {
            cin >> x;
            sum += x;
            if (j==t-1)
                output.push_back(sum-(t-1));
        }
    }
    for (auto x: output)
        cout << x << endl;
    
    return 0;
}