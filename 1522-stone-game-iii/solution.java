class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;

        // dp[i] = maximum score difference current player can get from index i
        int[] dp = new int[n + 1];

        // Fill from back to front
        for (int i = n - 1; i >= 0; i--) {
            dp[i] = Integer.MIN_VALUE;
            int sum = 0;

            // Try taking 1, 2, or 3 stones
            for (int k = 0; k < 3 && i + k < n; k++) {
                sum += stoneValue[i + k];

                // Current player's gain - opponent's best difference
                dp[i] = Math.max(dp[i], sum - dp[i + k + 1]);
            }
        }

        // Decide winner
        if (dp[0] > 0) {
            return "Alice";
        } else if (dp[0] < 0) {
            return "Bob";
        } else {
            return "Tie";
        }
    }
}
