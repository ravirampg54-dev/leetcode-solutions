// Get the lexicographically smallest string (in ascending order)
char* getMinString(const int* cnt) {
    int totalLen = 0;
    for (int i = 0; i < 26; i++) {
        totalLen += cnt[i];
    }

    char* res = (char*)malloc(totalLen + 1);
    int pos = 0;
    for (int i = 0; i < 26; i++) {
        if (cnt[i] > 0) {
            memset(res + pos, 'a' + i, cnt[i]);
            pos += cnt[i];
        }
    }
    res[pos] = '\0';
    return res;
}

// Get the maximum lexicographical string (in descending order)
char* getMaxString(const int* cnt) {
    int totalLen = 0;
    for (int i = 0; i < 26; i++) {
        totalLen += cnt[i];
    }

    char* res = (char*)malloc(totalLen + 1);
    int pos = 0;
    for (int i = 25; i >= 0; i--) {
        if (cnt[i] > 0) {
            memset(res + pos, 'a' + i, cnt[i]);
            pos += cnt[i];
        }
    }
    res[pos] = '\0';
    return res;
}

// Check if the remaining characters can form a string greater than the suffix.
bool canFormGreater(const int* cnt, const char* target, int start) {
    char* maxStr = getMaxString(cnt);
    bool result = strcmp(maxStr, target + start) > 0;
    free(maxStr);
    return result;
}

char* lexGreaterPermutation(char* s, char* target) {
    int cnt[26] = {0};
    for (int i = 0; s[i] != '\0'; i++) {
        cnt[s[i] - 'a']++;
    }

    int n = strlen(target);
    char* res = (char*)malloc(n + 27);
    int pos = 0;

    for (int i = 0; i < n; i++) {
        int targetChar = target[i] - 'a';

        // Case 1: First try to place the same character as target[i] at the
        // current position
        if (cnt[targetChar] > 0) {
            cnt[targetChar]--;
            // Check if the remaining characters can form a string greater than
            // target[i+1:]
            if (canFormGreater(cnt, target, i + 1)) {
                res[pos++] = target[i];
                continue;
            }
            // Cannot form a larger string, backtrack
            cnt[targetChar]++;
        }

        // Case 2: Place a character greater than target[i] at the current
        // position
        for (int j = targetChar + 1; j < 26; j++) {
            if (cnt[j] > 0) {
                cnt[j]--;
                res[pos++] = 'a' + j;
                // Fill remaining positions with the smallest lexicographical
                // order
                char* str = getMinString(cnt);
                strcpy(res + pos, str);
                free(str);
                return res;
            }
        }

        // No feasible solution found, return directly
        break;
    }

    free(res);
    return strdup("");
}
