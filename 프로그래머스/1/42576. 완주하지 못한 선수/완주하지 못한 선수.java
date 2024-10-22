import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 1. 배열 2개 정렬
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        // 배열 다를 때까지 찾기
        int i;
        for (i = 0; i < completion.length; i++) {
            if(!participant[i].equals(completion[i])){
                break;
            }
        }
        return participant[i];
    }
}