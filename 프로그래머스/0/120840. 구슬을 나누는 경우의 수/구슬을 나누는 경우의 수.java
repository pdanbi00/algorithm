class Solution {
    public int solution(int balls, int share) {
        int answer = 0;
        if (share > balls / 2) {
            share = balls - share;
        }
        
        double up = 1.0;
        for (int i = balls; i > balls-share; i--) {
            up *= i;
        }
        double down = 1.0;
        for (int i = 1; i <= share; i++) {
            down *= i;
        }
        double tmp = up / down;
        answer = (int) tmp;
        return answer;
    }
}