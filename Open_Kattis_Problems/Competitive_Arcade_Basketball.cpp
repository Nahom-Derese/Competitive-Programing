#include <bits/stdc++.h>
using namespace std;


int main()
{
    string s,T;
    map<string,int> Players;
    vector<string> ans;
    int a, b, c;
    cin >> a >> b >> c;
    string name;
    for (int i = 0; i < a; i++){
        cin >> name;
        Players[name]=0;
    }
    
    for (int i = 0; i < c; i++)
    {
        string y;
        int W;
        cin >> y >> W;
        Players[y] += W;
        bool flag = false;
        for (auto e: ans)
        {
            if (y + " wins!" == e)
                flag = true;
        }
        
        if (Players[y]>=b && !flag)
            ans.push_back(y + " wins!");
    }

    for (auto i:ans)
        cout << i << endl;


    if( ans.empty() )
        cout << "No winner!" << endl;
    
    return 0;
}