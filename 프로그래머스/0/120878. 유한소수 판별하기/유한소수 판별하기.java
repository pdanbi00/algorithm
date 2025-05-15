import java.util.*;
class Solution {
    public int solution(int a, int b) {
        int answer = 1;
        int tmp = 1;
        for (int i = 2; i <= Math.min(a, b); i++) {
            if (a % i == 0 && b % i == 0) {
                tmp = i;
            }
        }
        a /= tmp;
        b /= tmp;
        List<Integer> list = new ArrayList<>();
        for (int i = 2; i <= b; i++) {
            if (b % i == 0) {
                list.add(i);
            }
        }
        
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) % 2 == 0 || list.get(i) % 5 == 0) {
                continue;
            } else {
                answer = 2;
            }
        }
        
        return answer;
    }
}