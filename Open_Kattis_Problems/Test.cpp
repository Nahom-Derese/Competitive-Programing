#include <bits/stdc++.h>
using namespace std;
vector<int> primes;
bool prime(int m);
int main() {
    int z;
    cin >> z;
    
    for (int k = 2; k <= z; k++)
        primes.push_back(k);
    
    for (int i = 2; i*i < z+1; i++)
    {
        if (prime(i))
        {
            for (int j = 2; j*i < z; j++)
                primes.erase(remove(primes.begin(), primes.end(), j*i), primes.end());
        }
    }
    for (auto i:primes)
        cout << i << endl;
    

    return 0;
}

bool prime(int m){
    for (int i = 2; i*i < m+1; i++){
        if (m%i == 0)
            return false;
    }
    return true;
}