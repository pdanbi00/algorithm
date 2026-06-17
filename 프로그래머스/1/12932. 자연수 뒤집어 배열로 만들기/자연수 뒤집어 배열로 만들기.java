// class Solution {
//     public int[] solution(long n) {
//         String nStr = Long.toString(n);
//         int l = nStr.length();
//         int[] answer = new int[l];
//         for (int i = 0; i < l; i++) {
//             answer[i] = Character.getNumericValue(nStr.charAt(l-1-i));
//         }
//         return answer;
//     }
// }

class Solution {
    public int[] solution(long n) {
        int l = Long.toString(n).length();
        int[] answer = new int[l];
        for (int i = 0; i < l; i++) {
            Long tmp = n % 10;
            answer[i] = tmp.intValue();
            n /= 10;
        }
        return answer;
    }
}