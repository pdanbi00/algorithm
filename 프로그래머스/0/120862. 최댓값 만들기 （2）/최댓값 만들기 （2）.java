import java.util.Arrays;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
        int N = numbers.length;
        int tmp1 = numbers[0] * numbers[1];
        int tmp2 = numbers[N-1] * numbers[N-2];
        return Math.max(tmp1, tmp2);
    }
}