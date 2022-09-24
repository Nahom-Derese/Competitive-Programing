#include<bits/stdc++.h>
using namespace std;

int main(){
    int x;
    cin >> x;
    string name = x%2 != 0 ? "Alice" : "Bob";
    cout << name << endl;
    return 0;
    }