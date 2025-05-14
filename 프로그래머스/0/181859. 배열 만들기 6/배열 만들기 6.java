import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        List<Integer> stk = new ArrayList<>();
        int idx = 0;
        while (idx < arr.length) {
            if (stk.size() == 0) {
                stk.add(arr[idx]);
                idx++;
            } else if (stk.size() > 0 && stk.get(stk.size()-1) == arr[idx]) {
                stk.remove(stk.size()-1);
                idx++;
            } else {
                stk.add(arr[idx]);
                idx++;
            }
        }
        if (stk.size() == 0) {
            answer = new int[] {-1};
        } else {
            answer = new int[stk.size()];
            for (int i = 0; i < stk.size(); i++) {
                answer[i] = stk.get(i);
            }
        }
        
        
        return answer;
    }
}