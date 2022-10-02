#include <bits/stdc++.h>
using namespace std;

int main()
{
vector<int>ordered;
for (int i = 0; i < 3; i++)
        ordered.push_back(i);
        sort(ordered.begin(), ordered.end());
        cout << ordered[3/2] << endl;
    return 0;
}