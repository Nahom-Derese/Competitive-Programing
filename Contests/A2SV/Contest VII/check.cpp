#include <bits/stdc++.h>
using namespace std;

long long divide(long long a) {
    while (a % 2 == 0) a /= 2;
    while (a % 3 == 0) a /= 3;
    return a;   
}



int main() {
    int n;
    cin >> n;
    
    vector<long long> arr;
    for (long long i = 0; i < n; i++) {
        long long x;
        cin >> x;
        arr.push_back(divide(x));
    }
    
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] != arr[0]) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;

    return 0;
}