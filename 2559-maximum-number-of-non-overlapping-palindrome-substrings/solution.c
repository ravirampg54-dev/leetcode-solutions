int maxPalindromes(char* s, int k) {
    int n = strlen(s);
    bool** isPalindrome = (bool**)malloc(n * sizeof(bool*));
    for (int i = 0; i < n; i++) {
        isPalindrome[i] = (bool*)calloc(n, sizeof(bool));
    }

    for (int len = 1; len <= n; ++len) {
        for (int left = 0; left + len <= n; ++left) {
            int right = left + len - 1;
            isPalindrome[left][right] =
                (s[left] == s[right]) &&
                (len <= 2 || isPalindrome[left + 1][right - 1]);
        }
    }

    int* dp = (int*)calloc(n + 1, sizeof(int));
    for (int i = 1; i <= n; ++i) {
        dp[i] = dp[i - 1];
        for (int j = 0; j + k <= i; ++j) {
            if (isPalindrome[j][i - 1]) {
                dp[i] = dp[i] > dp[j] + 1 ? dp[i] : dp[j] + 1;
            }
        }
    }

    int result = dp[n];

    for (int i = 0; i < n; i++) {
        free(isPalindrome[i]);
    }
    free(isPalindrome);
    free(dp);

    return result;
}
