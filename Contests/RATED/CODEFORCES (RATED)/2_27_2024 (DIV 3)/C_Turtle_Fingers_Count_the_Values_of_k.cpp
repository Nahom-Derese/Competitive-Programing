#include <bits/stdc++.h>

using namespace std;

void divide(unordered_set<long long> &count, long long n, long long a, long long b){
    count.insert(n);
    // cout<<n<<" ";
    if (n%a==0){
        divide(count, n/a, a, b);
    }
    if (n%b==0){
        divide(count, n/b, a, b);
    }
}

int main() {
    int t;

    cin >> t;

    while (t--){
        long long l, a, b;
        cin >> a >> b >> l;
        unordered_set<long long> count;
        divide(count, l, a, b);
        cout << count.size() << endl;
    }
}

