#include<iostream>
#include<vector>
#include<utility>
#include<string>


using namespace std;


int main(){
    string input;
    cin >> input;
    double white=0,small=0,capital=0,symbols=0,count=0;
    for(auto i:input){
        white = i+0==95 ? white+1 : white;
        small = i+0>96 &&i+0<123 ? small+1 : small;
        capital = i+0>64 &&i+0<91 ? capital+1 : capital;
        symbols = (i+0<65) || (i+0>90 && i+0<97 && i+0!=95) || (i+0>122)? symbols+1 : symbols;
        count++;
    }
    double ans1,ans2,ans3,ans4;
    ans1 = white/count;
    ans2 = small/count;
    ans3 = capital/count;
    ans4 = symbols/count;
    printf("%.8f\n%.8f\n%.8f\n%.8f\n",ans1,ans2,ans3,ans4);
    return 0;
}