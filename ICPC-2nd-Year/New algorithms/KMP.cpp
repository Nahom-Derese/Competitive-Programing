#include<iostream>
#include<string>
#include<utility>

using namespace std;

int main(){
    string toBeSearched;
    string pattern;
    cin >> toBeSearched >> pattern;
    pair<char, int> lps[pattern.length() + 1];
    lps[0].first = '\0';
    lps[1].second = 0;
    
    for (int i = 0; i < pattern.length(); i++) {

        lps[i+1].first = pattern[i];

        if(i>0 && lps[i].second == 0 && lps[1].first == lps[i+1].first) 
            lps[i+1].second = lps[i].second + 1;

        if (i>0 && lps[i].second != 0 && lps[lps[i].second+1].first == lps[i+1].first) 
            lps[i+1].second = lps[i].second + 1;
    }
    
    for (int i = 1; i < sizeof(lps)/ sizeof(lps[0]); i++)
        cout << lps[i].first << " : " << lps[i].second << endl;
    int i = 0 ,j = 0, count = 0;
    
    while(i < toBeSearched.length()){
            if (toBeSearched[i] == lps[j+1].first)
            {
                i++;
                j++;
            }
            else if(j!=0){
                j = lps[j].second;
            }
            else{
                i++;
            }
            if(j==pattern.length()){ 
                count++;
                j = 0;
            }
        }
        
    cout << "No. of Occurence : " << count << endl; 
    
    return 0;
}