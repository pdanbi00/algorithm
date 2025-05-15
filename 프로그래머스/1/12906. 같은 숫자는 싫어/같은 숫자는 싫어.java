import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();
        for (int a : arr) {
            if (list.size() == 0) {
                list.add(a);
            } else {
                int tmp = list.get(list.size()-1);
                if (a != tmp) {
                    list.add(a);
                }
            }
        }
        answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}