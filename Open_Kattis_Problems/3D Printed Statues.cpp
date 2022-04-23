#include <bits/stdc++.h>
#define LOG(s) std::cout << s << std::endl;

using namespace std;

int main()
{
    int n, ans = 0;
    cin >> n;
    for (short i = 0; i < 15; i++)
    {
        if (pow(2, i) >= n)
        {
            ans = i + 1;
            break;
        }
    }

    LOG(ans);

    return 0;
}