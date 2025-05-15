import java.util.*;
class Solution {
    public int[] solution(int num, int total) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();
        
        if (num % 2 == 1) {
            int mid = total / num;
            list.add(mid);
            for (int k = 1; k <= num / 2; k++) {
                list.add(mid + k);
                list.add(mid - k);
            }
        } else {
            int mid = total / num;
            list.add(mid);
            for (int k = 1; k < num / 2; k++) {
                list.add(mid + k);
                list.add(mid - k);
            }
            list.add(mid + num/2);
        }
        Collections.sort(list);
        answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}