#include <bits/stdc++.h>
using namespace std;


int main()
{
    string action;
    int n;
    priority_queue<int> arr;
    while (cin >> action){
    if (action == "INSERT"){
        cin >> n;
        arr.push(n);}
    if (action == "REMOVE"){
        cout << arr.top() << endl;
        arr.pop();
    }
    if (action == "END"){
        for (int i = 0;i<arr.size();i++)
            arr.pop();
        cout << endl;
        }
    }
    return 0;
}