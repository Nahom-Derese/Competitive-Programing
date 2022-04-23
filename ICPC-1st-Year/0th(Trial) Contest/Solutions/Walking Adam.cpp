#include <iostream>
#include <cstring>
using namespace std;

int main(){
    int n;
    cin >> n;
    string arr[n];
    for (short i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    for (short i = 0; i < n; i++)
    {
        int count = 0;
        for (short j = 0; j < arr[i].length(); j++)
            {
                if(arr[i][j] == 'U'){
                    count+= 1;
                    if(j == arr[i].length()-1){
                        cout << count << endl;
                    }
                }else{
                    cout << count << endl;
                    break;
                }
            }
    }
    return 0;
}