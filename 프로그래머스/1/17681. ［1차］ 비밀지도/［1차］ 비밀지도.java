import java.util.ArrayList;
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        ArrayList<String> board1 = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String tmp = String.format("%0" + n + "d", Long.parseLong(Integer.toBinaryString(arr1[i]).toString()));
            board1.add(tmp);
        }
        
        ArrayList<String> board2 = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String tmp = String.format("%0" + n + "d", Long.parseLong(Integer.toBinaryString(arr2[i]).toString()));
            board2.add(tmp);
        }
        
        for (int i = 0; i < n; i++) {
            String tmp = "";
            for (int j = 0; j < n; j++) {
                if (board1.get(i).charAt(j) == '0' && board2.get(i).charAt(j) == '0') {
                    tmp += " ";
                } else {
                    tmp += "#";
                }
            }
            answer[i] = tmp;
        }
        return answer;
    }
}