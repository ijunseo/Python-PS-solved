#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, a = 1, b = 1;
    cin >> n;

    if (n % 2 != 0) {
        n --;
        a = a + n / 2;
        b = b + n / 2 + 1;
    } else {
        a = a + n / 2;
        b = b + n / 2;
    }

    cout << a * b;
    return 0;
}