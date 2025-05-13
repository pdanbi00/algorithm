class Solution {
    public int solution(String[] strArr) {
        int answer = 0;
        int[] len = new int[31];
        for (int i = 0; i < strArr.length; i++) {
            len[strArr[i].length()] += 1;
        }
        
        for (int i = 0; i < 31; i++) {
            answer = Math.max(answer, len[i]);
        }
        return answer;
    }
}