import java.util.*;
class Solution {
    public int solution(String number) {
        int answer = 0;
        int num = 0;
        for (int i = 0; i < number.length(); i++) {
            num += Character.getNumericValue(number.charAt(i));
        }
        answer = num % 9;
        return answer;
    }
}