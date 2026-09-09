class Solution {
    static int answer;
    public int solution(int n, int[][] q, int[] ans) {
        answer = 0;
        boolean[] used = new boolean[n+1];
        int[] nums = new int[5];
        func(0, 1, used, nums, n, q, ans);
        return answer;
    }
    static void func(int depth, int idx, boolean[] used, int[] nums, int n, int[][] q, int[] ans) {
        if (depth == 5) {
            for (int i = 0; i < q.length; i++) {
                int tmp = 0;
                for (int j = 0; j < 5; j++) {
                    for (int k = 0; k < 5; k++) {
                        if (q[i][k] == nums[j]) {
                            tmp++;
                        }
                    }
                }
                if (tmp != ans[i]) return;
            }
            answer++;
            return;
        } else {
            for (int i = idx; i <= n; i++) {
                if (!used[i]) {
                    used[i] = true;
                    nums[depth] = i;
                    func(depth+1, i+1, used, nums, n, q, ans);
                    nums[depth] = 0;
                    used[i] = false;
                }
            }
        }
    }
}