int* maxDepthAfterSplit(char* seq, int* returnSize) {
    int len = strlen(seq);
    int* ans = (int*)malloc(len * sizeof(int));
    int d = 0;
    int idx = 0;

    for (int i = 0; i < len; i++) {
        if (seq[i] == '(') {
            d++;
            ans[idx++] = d % 2;
        }
        if (seq[i] == ')') {
            ans[idx++] = d % 2;
            d--;
        }
    }

    *returnSize = idx;
    return ans;
}
