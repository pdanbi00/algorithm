import java.util.Set;
import java.util.HashSet;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {};
        int N = words.length;
        Set<String> used = new HashSet<>();
        boolean possible = true;
        
        for (int i = 0; i < N; i++) {
            if (used.contains(words[i])) {
                possible = false;
                if ((i+1) % n > 0) {
                    answer = new int[] {(i%n) + 1, (i+1) / n + 1};
                } else {
                    answer = new int[] {(i%n) + 1, (i+1) / n};
                }
                break;
            } else {
                if (i != 0) {
                     if (words[i].charAt(0) != words[i-1].charAt(words[i-1].length() - 1)) {
                        possible = false;
                        if ((i+1) % n > 0) {
                            answer = new int[] {(i%n) + 1, (i+1) / n + 1};
                        } else {
                            answer = new int[] {(i%n) + 1, (i+1) / n};
                        }
                        break;
                     }
                }
                used.add(words[i]);
            }  
        }
        if (possible) {
            answer = new int[] {0, 0};
        }
        return answer;
    }
}