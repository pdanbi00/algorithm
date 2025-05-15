import java.util.*;
class Solution {
    public int[] solution(int[] numlist, int n) {
        int[][] arr = new int[numlist.length][2];
        for (int i = 0; i < numlist.length; i++) {
            arr[i][0] = numlist[i];
            arr[i][1] = Math.abs(n - numlist[i]);
        }
        Arrays.sort(arr, (num1, num2) -> {
            if (num1[1] == num2[1]) {
                return num2[0] - num1[0];
            } else {
                return num1[1] - num2[1];
            }
        });
        int[] answer = new int[numlist.length];
        for (int i = 0; i < numlist.length; i++) {
            answer[i] = arr[i][0];
        }
        return answer;
    }
}