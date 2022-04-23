#include <bits/stdc++.h>
using namespace std;

float factorial (int x){
    float fact = 1;
    for (int i = 1; i < x+1; i++)
        fact *= i;
    
    return fact;
}

int main()
{
    for (int i = 0; i < 10; i++)
        cout << pow(i,i)/ (factorial(2*i)) << endl;
    
    return 0;
}