#include <iostream>
#include <cmath>

using namespace std;

bool rec(long long n, long long m){
    if (n == m){
        return true;
    }
    if (n < m){
        return false;
    }
    if ((n%3 == 0) || (((2*n)%3) == 0)){
        if (m == (2 * (n / 3)) || m == (n / 3)){
            return true;
        }
        return rec((n/3), m) || rec(2*(n/3), m);
    }
    return false;
}


int main(){
    int t;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        long long n, m;
        cin >> n >> m;
        
        if (rec(n, m)){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }
    

    return 0;
}