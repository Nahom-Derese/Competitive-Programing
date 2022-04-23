#include <bits/stdc++.h>
using namespace std;

int main(){
    int s,t,sum;
    sum = 0;
    cin >> s;
    for (short i = 0; i < s; i++)
    {
        cin >> t;
        sum += t;
        if(i!=0)
        sum--;
    }
    cout << sum << endl;
    
    return 0;
}