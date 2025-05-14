import java.util.*;
class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = {};
        List<Integer> arr = new ArrayList<>();
        
        if (n == 1) {
            for (int i = 0; i <= slicer[1]; i++) {
                arr.add(num_list[i]);
            }
        } else if (n == 2) {
            for (int i = slicer[0]; i < num_list.length; i++) {
                arr.add(num_list[i]);
            }
        } else if (n == 3) {
            for (int i = slicer[0]; i <= slicer[1]; i++) {
                arr.add(num_list[i]);
            }
        } else {
            for (int i = slicer[0]; i <= slicer[1]; i+=slicer[2]) {
                arr.add(num_list[i]);
            }
        }
        
        answer = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            answer[i] = arr.get(i);
        }
        
        return answer;
    }
}