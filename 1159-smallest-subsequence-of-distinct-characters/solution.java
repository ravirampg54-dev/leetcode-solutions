class Solution {
    public String smallestSubsequence(String s) {
        int[] lastIndex = new int[26];

        // Store last occurrence of each character
        for (int i = 0; i < s.length(); i++) {
            lastIndex[s.charAt(i) - 'a'] = i;
        }

        boolean[] visited = new boolean[26];
        StringBuilder stack = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (visited[c - 'a']) {
                continue;
            }

            while (stack.length() > 0 &&
                   stack.charAt(stack.length() - 1) > c &&
                   lastIndex[stack.charAt(stack.length() - 1) - 'a'] > i) {

                visited[stack.charAt(stack.length() - 1) - 'a'] = false;
                stack.deleteCharAt(stack.length() - 1);
            }

            stack.append(c);
            visited[c - 'a'] = true;
        }

        return stack.toString();
    }
}
