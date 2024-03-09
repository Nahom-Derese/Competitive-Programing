class Solution {
public:

    map<int, int> mem= {};
    int fib(int n) {
        // if ( mem.find(n) == mem.end() ) {
        if(!n) return 0;
        if(n == 1 || n==2) return 1;
        return fib(n-1) + fib(n-2);
        // }
        // else return mem[n];
    }
};