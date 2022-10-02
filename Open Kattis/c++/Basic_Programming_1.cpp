#include <bits/stdc++.h>
using namespace std;


int main()
{
    string s,m,T;
    int inputs[2], j;
    getline(cin, s);
    stringstream X(s);
    j = 0;
    while (getline(X, T, ' ')){
        inputs[j] = stoi(T);
        j++;
    }
    vector<int>Arr;
    getline(cin, m);
    stringstream Y(m);
    while (getline(Y, T, ' '))
        Arr.push_back(stoi(T));
    vector<int>ordered;
    map<int,char> alphabet;
    int i = Arr[0];
    int sum = 0;
    int even_sum = 0;
    switch (inputs[1])
    {
    case 1:
        cout << 7 << endl;
        break;
    case 2:
        if (Arr[0] > Arr[1])
            cout << "Bigger" << endl;
        else if (Arr[0] == Arr[1])
            cout << "Equal" << endl;
        else
            cout << "Smaller" << endl;
        break;
    case 3:
        for (int i = 0; i < 3; i++)
            ordered.push_back(Arr[i]);
        sort(ordered.begin(), ordered.end());
        cout << ordered[3/2] << endl;
        break;
    case 4:
        for (auto i:Arr)
          sum += i;  
        cout << sum << endl;
        break;
    case 5:
        for (auto i:Arr){
            if (i%2 == 0)
                even_sum +=i;
        }
        cout << even_sum << endl;
        break;
    case 6:
        alphabet[0] = 'a';
        alphabet[1] = 'b';
        alphabet[2] = 'c';
        alphabet[3] = 'd';
        alphabet[4] = 'e';
        alphabet[5] = 'f';
        alphabet[6] = 'g';
        alphabet[7] = 'h';
        alphabet[8] = 'i';
        alphabet[9] = 'j';
        alphabet[10] = 'k';
        alphabet[11] = 'l';
        alphabet[12] = 'm';
        alphabet[13] = 'n';
        alphabet[14] = 'o';
        alphabet[15] = 'p';
        alphabet[16] = 'q';
        alphabet[17] = 'r';
        alphabet[18] = 's';
        alphabet[19] = 't';
        alphabet[20] = 'u';
        alphabet[21] = 'v';
        alphabet[22] = 'w';
        alphabet[23] = 'x';
        alphabet[24] = 'y';
        alphabet[25] = 'z';
        for (auto i:Arr)
            cout << alphabet[i%26];
        cout << endl;
        break;
    case 7:
        while(Arr[i] < sizeof(Arr)/sizeof(Arr[0])-1){
            i = Arr[i];
            if (find(Arr.begin(), Arr.end(), i) - Arr.begin() == Arr[i]){
                cout << "Cyclic" << endl;
                break;
                }
            }
        if (find(Arr.begin(), Arr.end(), i) - Arr.begin() == Arr[i])
            break;
        if (i == sizeof(Arr)/sizeof(Arr[0]) -1)
            cout << "Done" << endl;
        else if(i != sizeof(Arr)/sizeof(Arr[0]) -1)
            cout << "Out" << endl;
        break;
    default:
        break;
    }
    return 0;
}