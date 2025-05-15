class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        int x1 = 300;
        int x2 = 300;
        int y1 = 300;
        int y2 = 300;
        
        for (int[] dot : dots) {
            if (x1 == 300) {
                x1 = dot[0];
            } else if (x1 != dot[0]) {
                x2 = dot[0];
            }
            if (y1 == 300) {
                y1 = dot[1];
            } else if (y1 != dot[1]) {
                y2 = dot[1];
            }
        }
        answer = Math.abs(x1 - x2) * Math.abs(y1 - y2);
        
        return answer;
    }
}