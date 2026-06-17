class Solution {
    public int[] solution(long n) {
        String nStr = Long.toString(n);
        int l = nStr.length();
        int[] answer = new int[l];
        for (int i = 0; i < l; i++) {
            answer[i] = Character.getNumericValue(nStr.charAt(l-1-i));
        }
        return answer;
    }
}