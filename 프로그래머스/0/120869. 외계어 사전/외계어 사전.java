class Solution {
    public int solution(String[] spell, String[] dic) {
        int answer = 2;
        boolean find = true;
        for (String word : dic) {
            find = true;
            if (spell.length == word.length()) {
                for (int i = 0; i < spell.length; i++) {
                    if (word.contains(spell[i])) {
                        continue;
                    } else {
                        find = false;
                        break;
                    }
                }
                if (find) {
                    return 1;
                }
            }
        }
        
        return answer;
    }
}