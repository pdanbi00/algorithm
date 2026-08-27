import java.util.ArrayList;
class Solution {
    static ArrayList<int[]> tmp;
    public int[][] solution(int n) {
        int[][] answer = {};
        tmp = new ArrayList<>();
        hanoi(1, 3, 2, n);
            
        answer = new int[tmp.size()][2];
        for (int i = 0; i < tmp.size(); i++) {
            answer[i][0] = tmp.get(i)[0];
            answer[i][1] = tmp.get(i)[1];
        }
        return answer;
    }
    
    static void hanoi(int start, int end, int extra, int cnt) {
        if (cnt == 1) {
            tmp.add(new int[]{start, end});
        } else {
            hanoi(start, extra, end, cnt-1);
            hanoi(start, end, extra, 1);
            hanoi(extra, end, start, cnt-1);
        }
        return;
    }
}