class Solution {
    public int[] solution(int n, int s) {
        int[] answer = {};
        int tmp = s / n;
        if (tmp == 0) {
            answer = new int[] {-1};
        } else {
            answer = new int[n];
            for (int i = 0; i < n; i++) {
                answer[i] = tmp;
                if (i >= n - (s % n)) {
                    answer[i]++;
                }
            }
        }
        return answer;
    }
}