#include <bits/stdc++.h>
using namespace std;
int input(){
    int _x;
    cin >> _x;
    return _x;
}

int main(){
    int i,n = input();
    vector<int> list(n);
    
    for (i = 0; i < n; i ++){
        cin >> list[i];
    }
    
    int ans_min, ans_max;
    
    ans_min = *min_element(list.begin(), list.end());;
    ans_max = *max_element(list.begin(), list.end());;
    cout << ans_min << " " << ans_max;
}