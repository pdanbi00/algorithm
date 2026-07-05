import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        ArrayList<Integer> tmp = new ArrayList<>();
        Arrays.sort(arr);
        for (int num : arr) {
            if (num % divisor == 0) {
                tmp.add(num);
            }
        }
        
        if (tmp.size() == 0) {
            answer = new int[] {-1};
        } else {
            answer = new int[tmp.size()];
            for (int i = 0; i < tmp.size(); i++) {
                answer[i] = tmp.get(i);
            }
        }
        
        return answer;
    }
}