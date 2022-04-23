#include<iostream>
#include<string>
#include<regex>
#include<cmath>
#include<vector>

int max_no(std::string n1, std::string n2, std::string n3);

int main(){
    int a;
    char y;
    std::string b;
    std::cin >> a;
    std::vector<int> w(0);
    std::vector<std::vector<int>> ans(a);
    std::fill(ans.begin(), ans.end(), w);
    std::cin.ignore();
    for (int i = 0; i < a; i++)
    {
        getline(std::cin, b);
        std::regex T("(\\w+)\\s([+/*-])\\s(\\w+)\\s=\\s(\\w+)");
        for(std::sregex_iterator o = std::sregex_iterator(b.begin(), b.end(), T); o != std::sregex_iterator(); o++)
        {
            std::smatch x = *o;
            std::string num1 = x.str(1);
            bool flag= false;
            int e = x.str(2) == "+" ? 1 : x.str(2) == "-" ? 2 : x.str(2) == "*" ? 3 : 4;
            std::string num2 = x.str(3);
            std::string num3 = x.str(4);
            int r = max_no(num1, num2, num3);
            for (int q = 1; q < 37; q++)
            {
                long double num_1 = 0, num_2 = 0, num_3 =0;
                for (long unsigned int j = 0; j != num1.length(); j++)
                {
                    if (num1[j]+0 >= 97 && num1[j]+0 < 124) num_1 += (num1[j]-87) * pow(q, num1.length()-j-1);
                    else if (num1[j]+0 >= 48 && num1[j]+0 < 58) num_1 += (num1[j]-48) * pow(q, num1.length()-j-1);
                    if (num1.length()-1 == j && e>2 ){if(r < q) flag = true;}
                    else if (num1.length()-1 == j && e<3 )if(r <= q) flag = true;
                }
                for (long unsigned int k = 0; k != num2.length(); k++)
                {
                    if (num2[k]+0 >= 97 && num2[k]+0 < 124) num_2 += (num2[k]-87) * pow(q, num2.length()-k-1);
                    else if (num2[k]+0 >= 48 && num2[k]+0 < 58) num_2 += (num2[k]-48) * pow(q, num2.length()-k-1);
                    if (num2.length()-1 == k && e>2 ){if(r < q) flag = true;}
                    else if (num2.length()-1 == k && e<3 )if(r <= q) flag = true;
                }
                for (long unsigned int p = 0; p != num3.length(); p++)
                {
                    if (num3[p]+0 >= 97 && num3[p]+0 < 124) num_3 += (num3[p]-87) * pow(q, num3.length()-p-1);
                    else if (num3[p]+0 >= 48 && num3[p]+0 < 58) num_3 += (num3[p]-48) * pow(q, num3.length()-p-1);
                    if (num3.length()-1 == p && e>2 ){if(r < q) flag = true;}
                    else if (num3.length()-1 == p && e<3 )if(r <= q) flag = true;
                }
                
                switch (e)
                {
                case 1:
                    if(num_1 + num_2 == num_3 && flag) ans[i].push_back(q);
                    break;
                case 2:
                    if(num_1 - num_2 == num_3 && flag) ans[i].push_back(q);
                    break;
                case 3:
                    if(num_1 * num_2 == num_3 && flag) ans[i].push_back(q);
                    break;
                case 4:
                    if(num_1 / num_2 == num_3 && flag) ans[i].push_back(q);
                    break;
                default:
                    break;
                }   
            }
        }
        
    }
    
    for (auto i : ans)
    {
        if (i.empty()) std::cout << "invalid";
        
        for (auto j:i)
        {
            j = j==36 ? 0:j;
            if (j>9) {y=j+87; std::cout << y;}
            else std::cout << j;
        }
        std::cout << std::endl;
    }
    
    return 0;
}

int max_no(std::string n1, std::string n2, std::string n3){
    
    std::string arr[3] = {n1,n2,n3};
    int r=0;

    for(auto a:arr){
        for (long unsigned int j = 0; j != a.length(); j++)
            {
                if (a[j]+0 >= 97) {if(a[j]-87 > r) r = a[j]-87;}
                else if (a[j]+0 >= 48 && (int)a[j]-48 > r) r = a[j]-48;
            }
    }

    return r;
}