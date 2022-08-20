#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> weight(n);
    vector<int> num(n);
    int sum = 0;
    for(int i = 0; i < n; i++){
        cin>>weight[i];
    }
    for(int i = 0; i < n; i++){
        cin >> num[i];
        sum += num[i]*weight[i];
    }
    vector<int>dp(sum+1, 0);
    dp[0] = 1;
    for(int i = 0; i < n; i++){
        for (int j = 0; j < num[i]; ++j) {
            for (int k = sum; k >= weight[i] ; --k) {
                if(dp[k-weight[i]] == 1)
                    dp[k] = 1;
            }
        }
    }
    int count = 0;
    for(auto iter = dp.begin(); iter != dp.end(); iter++){
        count += *iter;
    }
    cout << count;
    return 0;
}
