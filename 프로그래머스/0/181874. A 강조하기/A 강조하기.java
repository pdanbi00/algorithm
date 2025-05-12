class Solution {
    public String solution(String myString) {
        String answer = myString.toLowerCase();
        // for (char c : myString.toCharArray()) {
        //     if (c == 'a') {
        //         answer += 'A';
        //     } else if (Character.isUpperCase(c) && c != 'A') {
        //         answer += Character.toLowerCase(c);
        //     } else {
        //         answer += c;
        //     }
        // }
        answer = answer.replace('a', 'A');
        return answer;
    }
}