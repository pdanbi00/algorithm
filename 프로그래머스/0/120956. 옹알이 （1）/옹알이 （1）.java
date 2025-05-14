class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] talk = {"aya", "ye", "woo", "ma"};
        
        for (int i = 0; i < babbling.length; i++) {
            for (int j = 0; j < talk.length; j++) {
                babbling[i] = babbling[i].replace(talk[j], " ");
            }
            if (babbling[i].trim().length() == 0) {
                answer += 1;
            }
        }
        
        return answer;
    }
}