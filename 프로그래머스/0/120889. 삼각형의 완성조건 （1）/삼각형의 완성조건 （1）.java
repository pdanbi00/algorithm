class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int maxValue = 0;
        int maxIdx = 0;
        int tmp = 0;
        for (int i = 0; i < 3; i++) {
            if (sides[i] > maxValue) {
                maxValue = sides[i];
                maxIdx = i;
            }
        }
        for (int i = 0; i < 3; i++) {
            if (i != maxIdx) {
                tmp += sides[i];
            }
        }
        
        if (maxValue < tmp) {
            answer = 1;
        } else {
            answer = 2;
        }
        
        return answer;
    }
}