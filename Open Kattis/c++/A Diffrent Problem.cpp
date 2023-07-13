#include<iostream>


using namespace std;

int main(){
    long long int n,m;
    while(cin >> n >> m){
        long long int ans = m-n;
        if (ans > 0) cout << ans << endl;
        else cout << -1 * ans << endl;
    }
    return 0;
}