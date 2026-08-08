int* validSequence(char* word1, char* word2, int* returnSize) {
    int n = strlen(word1), m = strlen(word2);
    int* last = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) last[i] = -1;
    int j = m - 1;
    for (int i = n - 1; i >= 0; --i) {
        if (j >= 0 && word1[i] == word2[j]) {
            last[j] = i;
            j -= 1;
        }
    }
    int* res = (int*)malloc(m * sizeof(int));
    int skip = 0;
    j = 0;
    for (int i = 0; i < n; ++i) {
        if (j == m) break;
        if (word1[i] == word2[j] ||
            (skip == 0 && (j == m - 1 || i < last[j + 1]))) {
            skip += (word1[i] != word2[j] ? 1 : 0);
            res[j] = i;
            j += 1;
        }
    }
    free(last);
    if (j == m) {
        *returnSize = m;
        return res;
    }
    *returnSize = 0;
    free(res);
    return NULL;
}
