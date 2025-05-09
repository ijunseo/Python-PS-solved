#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> lst(n);
    for (int i = 0; i < n; i ++){
        int now;
        cin >> now;
        lst[i] = now;
    }

    int ans = 0;
    int piv = 1;

    for (int i = 0; i < n; i ++){
        int now = lst[i];
        if (now == 1){
            ans += piv;
            piv ++;
        }
        else{
            piv = 1;
        }
    }

    cout << ans;
    return 0;
}