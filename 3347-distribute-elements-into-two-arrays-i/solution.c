int* resultArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* arr1 = (int*)malloc(sizeof(int) * numsSize);
    int* arr2 = (int*)malloc(sizeof(int) * numsSize);
    int idx1 = 0, idx2 = 0;
    arr1[idx1++] = nums[0];
    arr2[idx2++] = nums[1];
    for (int i = 2; i < numsSize; i++) {
        if (arr1[idx1 - 1] > arr2[idx2 - 1]) {
            arr1[idx1++] = nums[i];
        } else {
            arr2[idx2++] = nums[i];
        }
    }
    int* res = (int*)malloc(sizeof(int) * numsSize);
    int pos = 0;
    for (int i = 0; i < idx1; i++) {
        res[pos++] = arr1[i];
    }
    for (int i = 0; i < idx2; i++) {
        res[pos++] = arr2[i];
    }
    free(arr1);
    free(arr2);
    return res;
}
