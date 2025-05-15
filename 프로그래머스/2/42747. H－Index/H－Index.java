import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int n = citations.length;
        Arrays.sort(citations);
        for (int i = 0; i < n-1; i++) {
            int tmp = n - i;
            if (citations[i] >= tmp) {
                answer = tmp;
                break;
            }
        }
        return answer;
    }
}