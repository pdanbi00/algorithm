class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = {};
        
        int N = wallpaper.length;
        int M = wallpaper[0].length();
        
        int lux = N;
        int luy = M;
        int rux = 0;
        int ruy = 0;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    lux = Math.min(lux, i);
                    luy = Math.min(luy, j);
                    rux = Math.max(rux, i);
                    ruy = Math.max(ruy, j);
                }
            }
        }
        answer = new int[] {lux, luy, rux+1, ruy+1};
        return answer;
    }
}