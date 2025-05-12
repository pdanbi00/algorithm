import java.util.*;
class Solution {
    public List solution(int[] arr, int[] delete_list) {
        List<Integer> answer = new ArrayList<>();
        boolean possible = true;
        for (int i = 0; i < arr.length; i++) {
            possible = true;
            for (int j = 0; j < delete_list.length; j++) {
                if (arr[i] == delete_list[j]) {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                answer.add(arr[i]);
            }
        }
        return answer;
    }
}