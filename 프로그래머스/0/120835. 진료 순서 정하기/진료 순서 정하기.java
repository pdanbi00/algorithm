import java.util.Arrays;
class Solution {
    public int[] solution(int[] emergency) {
        int N = emergency.length;
        int[] answer = new int[N];
        int[] sorted = new int[N];
        for (int i = 0; i < N; i++) {
            sorted[i] = emergency[i];
        }
        Arrays.sort(sorted);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (emergency[i] == sorted[j]) {
                    answer[i] = N-j;
                    break;
                }
            }
        }
        return answer;
    }
}