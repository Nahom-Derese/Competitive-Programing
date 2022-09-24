#include<iostream>
#include<vector>
#include<utility>
#include<string>


using namespace std;


int main(){
    int m,n;
    cin >> m >> n;
    if ((4*m + 3*n)%2 == 0) cout << "possible" << endl;
    else cout << "impossible" << endl;
    
    return 0;
}