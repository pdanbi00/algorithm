class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] ranks = new int[n][n];
        
        for (int i = 0; i < results.length; i++) {
            int[] rank = results[i];
            ranks[rank[0]-1][rank[1]-1] = 1;
            ranks[rank[1]-1][rank[0]-1] = -1;
        }
        
        
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (i == j) continue;
                    
                    if (ranks[i][j] != 0) continue;
                    
                    if (ranks[i][k] == 1 && ranks[k][j] == 1) {
                        ranks[i][j] = 1;
                        ranks[j][i] = -1;
                    }
                }
            }
        }
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (ranks[i][j] == 0) cnt++;
            }
            
            if (cnt == 1) answer++;
        }
        
        return answer;
    }
}