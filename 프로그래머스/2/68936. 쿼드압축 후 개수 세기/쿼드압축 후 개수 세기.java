class Solution {
    static int[] answer;
    public int[] solution(int[][] arr) {
        answer = new int[2];
        func(0, 0, arr.length, arr);
        return answer;
    }
    static void func(int r, int c, int k, int[][] arr) {
        if (k == 1) {
            answer[arr[r][c]]++;
            return;
        }
        
        boolean possible = true;
        int target = arr[r][c];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                if (arr[r+i][c+j] != target) {
                    possible = false;
                    break;
                }
            }
            if (!possible) break;
        }
        
        if (possible) {
            answer[target]++;
            return;
        }
        
        int tmp = (int) k/2;
        func(r, c, tmp, arr);
        func(r+tmp, c, tmp, arr);
        func(r, c+tmp, tmp, arr);
        func(r+tmp, c+tmp, tmp, arr);
        
    }
}