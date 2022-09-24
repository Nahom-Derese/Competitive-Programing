#include<iostream>
using namespace std;

int main(){
    
    int nums[3];
    char char1,char2,char3;

    for (short i = 0; i < 3; i++)
        cin >> nums[i];
    cin >> char1 >> char2 >> char3;

    int flag = char1+0 > char2+0 && char2+0 > char3+0 ? 1 : char1+0 < char2+0 && char2+0 < char3+0 ? 2 : char1+0 > char2+0 && char2+0 < char3+0 ? 3 : 4;
    //                   C  B  A                             A  B  C                     C A B or  B A C                     A C B  or  B C A   
    
    // Sorting the numbers
    for (short i = 0; i < 3; i++)
    {
        for (short j = 0; j < 3; j++)
        {
            if(nums[i] < nums[j]){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
        
    }
    
    
    switch (flag)
    {
    case 1:
        cout << nums[2] << ' ' << nums [1] << ' ' << nums[0] << endl;
        break;
    case 2:
        cout << nums[0] << ' ' << nums [1] << ' ' << nums[2] << endl;
        break;
    case 3:
        if (char1+0 > char3+0)
            cout << nums[2] << ' ' << nums [0] << ' ' << nums[1] << endl;
        else
            cout << nums[1] << ' ' << nums [0] << ' ' << nums[2] << endl;
        break;
    case 4:
        if (char1+0 > char3+0)
            cout << nums[1] << ' ' << nums [2] << ' ' << nums[0] << endl;
        else
            cout << nums[0] << ' ' << nums [2] << ' ' << nums[1] << endl;
        break;
    default:
        break;
    }

    return 0;
}