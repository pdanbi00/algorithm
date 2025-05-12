class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String arr = "";
        for (char c : myString.toCharArray()) {
            if (c == 'A') {
                arr += 'B';
            } else {
                arr += 'A';
            }
        }
        if (arr.contains(pat)) {
            answer = 1;
        } else {
            answer = 0;
        }
        
        return answer;
    }
}