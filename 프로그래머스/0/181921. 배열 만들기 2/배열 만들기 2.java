import java.util.*;
class Solution {
    public int[] solution(int l, int r) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            String num = Integer.toString(i);
            boolean possible = true;
            for (int j = 0; j < num.length(); j++) {
                if (num.charAt(j) == '0' || num.charAt(j) == '5') {
                    continue;
                } else {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                list.add(i);
            }
        }
        if (list.size() == 0) {
            answer = new int[] {-1};
        } else {
            answer = new int[list.size()];
            for (int i = 0; i < list.size(); i++) {
                answer[i] = list.get(i);
            }
        }
        
        return answer;
    }
}