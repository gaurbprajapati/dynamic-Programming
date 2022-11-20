
# https://leetcode.com/problems/coin-change/

'''

#include <bits/stdc++.h>
using namespace std;
#define INF INT_MAX-1
class Solution {
public:
    int coinChange(vector<int>& coins, int sum) {
    int n=coins.size();
    int t[n + 1][sum + 1];
	// initialization
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= sum; j++) {
			if (j == 0)
				t[i][j] = 0;
			if (i == 0)
				t[i][j] = INF;
			if (i == 1) {
				if (j % coins[i - 1] == 0)
					t[i][j] = j / coins[i - 1];
				else
					t[i][j] = INF;
			}
		}
	}

	t[0][0] = 0;

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= sum; j++)
			if (coins[i - 1] <= j)
				t[i][j] = min(t[i - 1][j], 1 + t[i][j - coins[i - 1]]);
			else
				t[i][j] = t[i - 1][j];

	if(t[n][sum]==INF) {
        return -1;
    }else{
        return t[n][sum];
    }
    }
};

'''
