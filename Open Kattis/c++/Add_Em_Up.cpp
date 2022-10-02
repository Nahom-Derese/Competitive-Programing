#include<iostream>
#include<vector>
#include<utility>
#include<string>
#include<cmath>

using namespace std;

class Node
{
public:
    unsigned long long data;
    Node* Parent = NULL;
    Node* Right = NULL;
    Node* Left = NULL;
    bool L= false,R= false,N= false;
    Node(unsigned long long d);
    ~Node();
};

Node::Node(unsigned long long d)
{
    this->data = d;
}

Node::~Node()
{
    delete this;
}

class Tree{
public:
    Tree();
    Node* Head;
    int count;
    void add(unsigned long long data);
    vector<unsigned long long> in_order_traversal();
};

Tree::Tree(){
    Head = NULL;
}

void Tree::add(unsigned long long data){
    count++;
    Node* ad = new Node(data);
    Node* itr = Head;
    Node* parent = Head;
    if (Head==NULL) Head = ad;
    else {
        while (itr->Right != NULL || itr->Left != NULL)
        {
            if (ad->data >= itr->data) {
                parent = itr->Right == NULL ? itr : itr->Right;
                if (itr->Right == NULL) break;
                else itr = itr->Right;
            }
            else {
                parent = itr->Left == NULL ? itr : itr->Left;
                if (itr->Left == NULL) break;
                else itr = itr->Left;
            }
        }
        if(ad->data >= itr->data) itr->Right = ad;
        else itr->Left = ad;
        ad->Parent = parent;
    }
}

vector<unsigned long long> Tree::in_order_traversal(){
    vector<unsigned long long> ans;
    Node* itr = Head;
    while (ans.size() < count)
    {
        if (itr->Left == NULL) itr->L = true;
        if (itr->Right == NULL) itr->R = true;
        
        if (!(itr->L)) {
            itr->L = true;
            itr = itr->Left;
            continue;
        }
        
        else if(!(itr->N)) {
            itr->N = true;
            ans.push_back(itr->data);
            continue;
        }
        
        else if(!(itr->R)){
            itr->R = true;
            itr = itr->Right;
            continue;
        }
        
        else itr = itr->Parent;
    }

    return ans;
}

unsigned long long up_side_down(unsigned long long data){
    string num = to_string(data);
    int length = num.length()-1;
    char itr;
    unsigned long long ans = 0;
    while (itr != '3' && itr != '4' && itr != '7' && length>=0)
    {
        itr = num[length];
        itr = itr == '9' ? '6' : itr == '6' ? '9' : itr;
        ans += (itr - '0') * pow(10,length);
        if (length == 0 && ans!=data) return ans;
        length--;
    }
    
    return 0;
}


int main(){
    int n,s;
    Tree* Data = new Tree();
    cin >> n >> s;
    for (int i = 0; i < n; i++)
    {
        unsigned long long d;
        cin >> d;
        Data->add(d);
        if (up_side_down(d)) Data->add(up_side_down(d));
    }
    
    for (int i = 0; i < n; i++)
        {
            vector<unsigned long long> a = Data->in_order_traversal();
            unsigned long long e = a[i];
            int l = 0, r = a.size()-1;
            while (l < r)
            {
                int h = (r+l)/2;
                if (r-l == 1){
                    if (e!=a[h] && (a[r] == s-e || a[l] == s-e)){ 
                        cout << "YES" << endl;
                        return 0;
                    }
                    else{
                        cout << "NO" << endl;
                        return 0;
                    }
                }
                if (a[h] > s-e) r = h;
                if (a[h] < s-e) l = h;
                if (e!=a[h] && (a[h] == s-e)){ 
                    cout << "YES" << endl;
                    return 0;
                }
            }
        }
        cout << "NO" << endl;
    return 0;
}