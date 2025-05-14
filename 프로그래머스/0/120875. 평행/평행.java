class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        double i;
        double j;
        i = (double) (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]);
        j = (double) (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0]);
        if (i == j) {
            answer = 1;
        }
        
        i = (double) (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0]);
        j = (double) (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0]);
        if (i == j) {
            answer = 1;
        }
        
        i = (double) (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0]);
        j = (double) (dots[1][1] - dots[2][1]) / (dots[2][0] - dots[2][0]);
        if (i == j) {
            answer = 1;
        }
        return answer;
    }
}