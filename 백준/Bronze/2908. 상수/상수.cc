#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> aa(3, 0);
    vector<int> bb(3, 0);
    string a, b;
    cin >> a >> b;
    for (int i = 0; i < 3; i ++){
        aa[i] = int(a[i] - '0');
        bb[i] = int(b[i] - '0');
    }
    reverse(aa.begin(), aa.end());
    reverse(bb.begin(), bb.end());

    for (int i = 0; i < 3; i ++){
        if (aa[i] > bb[i]) {
            for (int x : aa) cout << x;
            return 0;
        } else if (aa[i] < bb[i]) {
            for (int x : bb) cout << x;
            return 0;
        }
    }
    return 0;
}
