#include<bits/stdc++.h>
using namespace std;

double ans, sum = 0, A2L = pow(0.5,0.75), A2S = pow(0.5,1.25) , Area_of_A1 = 2* (A2L * A2S);

double Shorter_Side(int y);
double Longer_Side(int y);


int main(){
    
    int n, j = 0, counter;
    cin >> n;
    int m[n-1][2];

    for (int i = 0; i < n-1; i++){
        cin >> m[i][0];
        if( sum + m[i][0]*(Area_of_A1 / pow(2,i+1)) <= Area_of_A1 ){
            sum += m[i][0]*(Area_of_A1 / pow(2,i+1));
            m[i][1] = m[i][0];   
        }
        else{
            m[i][1] = (Area_of_A1 - sum) / (Area_of_A1 / pow(2,i+1));
            sum += m[i][1] * (Area_of_A1 / pow(2,i+1));
        }
    }

    if (sum == Area_of_A1)
    {
        for (int k = n-2; k > 0; k--){
            m[k-1][1] += m[k][1] / 2;
            ans += (m[k][1] / 2) * (Longer_Side(k));
        }
        ans += A2L;
        printf("%.8f\n",ans);
    }
    else
        cout << "impossible" << endl;
    

    return 0;
}

double Shorter_Side(int y){
    if(y == 0)
        return A2S;
    else
        return Longer_Side(y-1)/2;
}

double Longer_Side(int y){
    if(y == 0)
        return A2L;
    else
        return Shorter_Side(y-1);
}