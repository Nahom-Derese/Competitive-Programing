#include<bits/stdc++.h>

int main(){
    int a,c=1;
    std::cin >> a;
    for (short i = 2; i <= sqrt(a); i++)
    {
        if (a%i == 0)
        {
            a /= i;
            c++;
            i=1;
        }
    }
    

    std::cout << c << std::endl;
    return 0;
}