#include <bits/stdc++.h>


using namespace std;

vector<bool> Composite(1ull << 31, false);

void seiveGenerate() {
    long long limit = static_cast<long long>(1) << 31;
    for (long long i = 2; i * i < limit; i++) {
        if (Composite[i]) continue;
        else {
            for (long long j = i * 2; j < limit; j += i)
                Composite[j] = true;   
        }
    }
}



int main(){
    seiveGenerate();

    int y;

    while (cin >> y)
    {
        map<long long, long long> powers;
        int x = y;
        for (long long i = 2; i < abs(y); i++)
        {
            if(Composite[i]) continue;
            else{
                int count = 0;
                while(x%i == 0)
                {
                    x = x/i;
                    count++;
                }    
                if (count != 0) powers[i] += count;
                }
        }
        if (y < 0) cout << -1 << " ";
        if (powers.empty()) cout << abs(y);

        for (pair<long long, long long> l: powers)
        {
            cout << l.first;
            if (l.second != 1) cout << '^' << l.second << " ";
            else cout << " ";
        }
        cout << endl;
            
        }
        
    }
    
