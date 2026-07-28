import java.util.Arrays;
class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = 0;
        int[][] distance = new int[n+1][n+1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(distance[i], 20000001);
        }
        for (int i = 1; i <= n; i++) {
            distance[i][i] = 0;
        }
        
        for (int[] fare : fares) {
            distance[fare[0]][fare[1]] = fare[2];
            distance[fare[1]][fare[0]] = fare[2];
        }
        
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    distance[i][j] = Math.min(distance[i][j], distance[i][k] + distance[k][j]);
                }
            }
        }
        
        answer = distance[s][a] + distance[s][b];
        
        for (int k = 1; k <= n; k++) {
            answer = Math.min(answer, distance[s][k] + distance[k][a] + distance[k][b]);
        }
        
        return answer;
    }
}