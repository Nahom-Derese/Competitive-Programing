#include <bits/stdc++.h>
using namespace std;

vector<long long> prime_sieve(long long n) {
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (long long i = 2; i <= sqrt(n); i++) {
        if (is_prime[i]) {
            for (long long j = i * i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    vector<long long> primes;
    for (long long i = 2; i <= n; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
        }
    }
    return primes;
}


int main() {
    vector<long long> primes = prime_sieve(pow(10, 5));
    
   
    
    int t;
    cin >> t;
    
    while (t--) {
        long long a, b;
        cin >>  a >> b;
        long long diff = a - b;
        bool flag = false;
        for (long long i = 0; i < primes.size(); i++)
        {
            if (diff % primes[i] == 0){
                cout << "YES" << endl;
                flag = true;
                break;
            }
        }
        if (!flag) cout << "NO" << endl;
    
    }
    
    return 0;
}
