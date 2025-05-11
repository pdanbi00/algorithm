import java.util.*;
class Solution {
    public List solution(int[] num_list, int n) {
        List<Integer> answer = new ArrayList<>();
        int[] arr1 = new int[n];
        int[] arr2 = new int[num_list.length - n];
        
        for (int i = 0; i < num_list.length; i++) {
            if (i < n) {
                arr1[i] = num_list[i];
            } else {
                arr2[i-n] = num_list[i];
            }
        }
        for (int i = 0; i < arr2.length; i++) {
            answer.add(arr2[i]);
        }
        for (int i = 0; i < arr1.length; i++) {
            answer.add(arr1[i]);
        }
        return answer;
    }
}