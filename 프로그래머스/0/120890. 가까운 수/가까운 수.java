import java.util.Arrays;
class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int diff = 100;
        Arrays.sort(array);
        for (int i = 0; i < array.length; i++) {
            if (diff > Math.abs(n - array[i])) {
                diff = Math.abs(n - array[i]);
                answer = array[i];
            }
        }
        return answer;
    }
}