#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>

using namespace std;

int min_cut_cost(int l, vector<int>& cut_positions) {
    vector<int> cuts = {0};
    cuts.insert(cuts.end(), cut_positions.begin(), cut_positions.end());
    cuts.push_back(l);
    
    int n = cuts.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    for (int length = 2; length < n; ++length) { // The length of the segment
        for (int i = 0; i < n - length; ++i) {
            int j = i + length;
            dp[i][j] = numeric_limits<int>::max();
            for (int k = i + 1; k < j; ++k) {
                dp[i][j] = min(dp[i][j], (cuts[j] - cuts[i]) + dp[i][k] + dp[k][j]);
            }
        }
    }
    
    return dp[0][n - 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int l;
    while (cin >> l && l != 0) {
        int n;
        cin >> n;
        vector<int> c(n);
        for (int i = 0; i < n; ++i) {
            cin >> c[i];
        }
        
        cout << "The minimum cutting is " << min_cut_cost(l, c) <<"." << "\n" ;
    }
    
    return 0;
}
