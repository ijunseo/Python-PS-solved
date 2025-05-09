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

    int ans = n;

    for (int i = 0; i < n; i ++){
        int now = lst[i];
        if (now == 1){
            ans --;
            continue;
        }
        for (int i = 2; i < now; i ++){

            if (now % i == 0){
                ans--;
                break;
            }
        }
    }

    cout << ans;
    return 0;
}