import java.util.Arrays;
import java.util.ArrayList;
class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        Arrays.sort(data, (o1, o2) -> (o1[col-1] == o2[col-1] ? o2[0]-o1[0] : o1[col-1] - o2[col-1]));
        int n = data[0].length;
        ArrayList<Integer> nums = new ArrayList<>();
        for (int i = row_begin; i <= row_end; i++) {
            int tmp = 0;
            for (int j = 0; j < n; j++) {
                tmp += data[i-1][j] % i;
            }
            nums.add(tmp);
        }
        answer = nums.get(0);
        
        for (int i = 1; i < nums.size(); i++) {
            answer = answer ^ nums.get(i);
        }
        
        
        return answer;
    }
}