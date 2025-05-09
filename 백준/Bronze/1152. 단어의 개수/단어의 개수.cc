#include <iostream>
#include <vector>
using namespace std;

int main(){
    string n;
    getline(cin , n);
    int ans = 1;
    for (int i = 0; i < n.size(); i ++){
        char now = n[i];
        if (n.size() == 1 && now == ' '){
            ans = 0;
        }
        if (i == 0 && now == ' ' || i == n.size() - 1 && now == ' '){
            continue;
        }
        if (now == ' '){
            ans ++;
        }
    }

    cout << ans;
    return 0;
}