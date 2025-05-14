import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        List<Integer> index = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                index.add(i);
            }
        }
        if (index.size() == 0) {
            answer = new int[] {-1};
        } else if (index.size() == 1) {
            answer = new int[] {2};
        } else {
            answer = new int[index.get(index.size() - 1) - index.get(0) + 1];
            for (int i = 0 ; i < answer.length; i++) {
                answer[i] = arr[index.get(0) + i];
            }
               
        }
        return answer;
    }
}