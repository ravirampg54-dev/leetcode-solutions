class Solution {
    public int[] gcdValues(int[] nums, long[] queries) {

        int max = 0;
        for (int x : nums)
            max = Math.max(max, x);

        int[] freq = new int[max + 1];

        for (int x : nums)
            freq[x]++;

        int[] divisible = new int[max + 1];

        // count numbers divisible by i
        for (int i = 1; i <= max; i++) {
            for (int j = i; j <= max; j += i) {
                divisible[i] += freq[j];
            }
        }

        long[] exact = new long[max + 1];

        // inclusion-exclusion
        for (int i = max; i >= 1; i--) {

            long cnt = divisible[i];

            exact[i] = cnt * (cnt - 1) / 2;

            for (int j = i + i; j <= max; j += i) {
                exact[i] -= exact[j];
            }
        }

        long[] prefix = new long[max + 1];

        for (int i = 1; i <= max; i++) {
            prefix[i] = prefix[i - 1] + exact[i];
        }

        int[] ans = new int[queries.length];

        for (int k = 0; k < queries.length; k++) {

            long target = queries[k];

            int lo = 1;
            int hi = max;

            while (lo < hi) {
                int mid = (lo + hi) / 2;

                if (prefix[mid] > target)
                    hi = mid;
                else
                    lo = mid + 1;
            }

            ans[k] = lo;
        }

        return ans;
    }
}
