class Solution {
    public int solution(int[][] arr) {
        int answer = 0;
        boolean possible = true;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i][j] != arr[j][i]) {
                    possible = false;
                    break;
                }
            }
            if (!possible) {
                break;
            }
        }
        
        if (possible) {
            answer = 1;
        }
        return answer;
    }
}