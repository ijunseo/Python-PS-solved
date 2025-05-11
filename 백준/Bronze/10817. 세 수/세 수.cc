#include <bits/stdc++.h>
using namespace std;
int main(){
    vector<int> list(3, 0);
    for(int i = 0; i < 3; i ++){
        cin >> list[i];
    }
    sort(list.begin(), list.end());
    cout << list[1];
}