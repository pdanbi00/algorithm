class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        int[] rail = new int[200];
        for (int[] line : lines) {
            for (int j = line[0] + 100; j < line[1] + 100; j++) {
                rail[j] ++;
            }
        }
        
        for (int i = 0; i < 200; i++) {
            if (rail[i] > 1) {
                answer += 1;
            }
        }
        return answer;
    }
}