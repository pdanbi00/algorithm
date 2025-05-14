class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        if (n == 1) {
            answer[0][0] = 1;
        }
        else {
            int num = 1;
            for (int k = 0; k < n/2; k++) {
                // 제일 위 행 (k행 k열 ~ n-1-k열 n-(2*k)열 동안 )
                for (int j = k; j < n-k; j++) {
                    answer[k][j] = num;
                    num += 1;
                }

                // 제일 오른쪽 열 (n-1-k열 k+1행 ~ n-1-k행)
                for (int i = k+1; i < n-k; i++) {
                    answer[i][n-1-k] = num;
                    num += 1;
                }

                // 제일 아래쪽 행 (n-1-k행 n-1-k-1열 ~ k열)
                for (int j = n-1-k-1; j >= k; j--) {
                    answer[n-1-k][j] = num;
                    num += 1;
                }

                // 제일 왼쪽 열 (k열 n-1-k-1행 ~ k+1행)
                for (int i = n-1-k-1; i >= k+1; i--) {
                    answer[i][k] = num;
                    num += 1;
                }

            }
            if (n % 2 == 1) {
                System.out.print(n/2);
                answer[n/2][n/2] = num;
            }
        }
        
        return answer;
    }
}