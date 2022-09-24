#include<bits/stdc++.h>

int main(){
    int a,b,c,d;
    std::cin >> a >> b >> c;
    bool e[a];
    for (short i = 0; i < a; i++)
    {
        std::cin >> d;
        if (d <= pow(pow(b,2) + pow(c,2) , 0.5))
            e[i] = true;
        else
            e[i] = false;
    }
    for (short i = 0; i < a; i++)
    {
        if(e[i])
            std::cout << "DA" << std::endl;
        else
            std::cout << "NE" << std::endl;
    }
    
}