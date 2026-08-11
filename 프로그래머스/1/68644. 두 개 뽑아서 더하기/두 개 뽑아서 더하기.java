import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;
class Solution {
    public int[] solution(int[] numbers) {
        Integer[] tmp = {};
        int[] answer = {};
        int N = numbers.length;
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < N-1; i++) {
            for (int j = i+1; j < N; j++) {
                set.add(numbers[i] + numbers[j]);
            }
        }
        tmp = set.toArray(new Integer[0]);
        answer = new int[tmp.length];
        for (int i = 0; i < tmp.length; i++) {
            answer[i] = tmp[i];
        }
        Arrays.sort(answer);
        return answer;
    }
}