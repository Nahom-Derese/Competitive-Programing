#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;

bool check[1000000];

int main() {
    unsigned int N, Q, n;
    bool c = false;
    unsigned int last_reset[2] = {0,0};
    string Y;
    cin >> N >> Q;
    unordered_map<unsigned int,pair<unsigned int,unsigned int>> J;
    vector<unsigned int> H;
    for (unsigned int i = 0; i < Q; i++)
    {
        cin >> Y >> n;
        int m = Y=="SET" ? 1:Y=="RESTART"? 2:3, u;
        switch (m)
        {
        case 1:
            cin >> u;
            check[n-1] = true;
            J[n] = {u,i+1};
            break;
        case 2:
            c = true;
            last_reset[0] = n;
            last_reset[1] = i+1;
            break;
        case 3:
            if (c && check[n-1] && last_reset[1] > J[n].second)
                H.push_back(last_reset[0]);
            else if (c && check[n-1] && last_reset[1] < J[n].second)
                H.push_back(J[n].first);
            else if(check[n-1] && !c)
                H.push_back(J[n].first);
            else if(!check[n-1] && c)
                H.push_back(last_reset[0]);
            else
                H.push_back(0);
            break;
        default:
            break;
        }
    }
    
    for (auto i:H)
        cout << i << endl;
    
    return 0;
}