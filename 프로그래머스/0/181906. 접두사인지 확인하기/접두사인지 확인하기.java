class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
        boolean possible = true;
        if (my_string.length() < is_prefix.length()) {
            possible = false;
        } else {
            for (int i = 0; i < is_prefix.length(); i++) {
                if (my_string.charAt(i) != is_prefix.charAt(i)) {
                    possible = false;
                    break;
                }
            }
        }
        
        if (possible) {
            answer = 1;
        }
        return answer;
    }
}