#include <bits/stdc++.h>
using namespace std;


int main(){
    int n;
    int ans = 1;
    cin >> n;
    for (int i = 1; i < n; i ++){
        ans *= i + 1;
    }

    cout << ans;
    return 0;
}