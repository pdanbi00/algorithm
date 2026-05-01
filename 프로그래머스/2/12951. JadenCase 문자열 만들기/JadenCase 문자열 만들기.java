// import java.util.Character;
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split(" ");
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
            String tmp = "";
            for (int j = 0; j < arr[i].length(); j++) {
                if (j == 0 && Character.isLetter(arr[i].charAt(j))) {
                    tmp += String.valueOf(arr[i].charAt(j)).toUpperCase();
                } else if (j == 0 && !Character.isLetter(arr[i].charAt(j))) {
                    tmp += arr[i].charAt(j);
                } else {
                    tmp += String.valueOf(arr[i].charAt(j)).toLowerCase();
                }
            }
            if (i < arr.length - 1) {
                answer += tmp + " ";
            } else {
                answer += tmp;
            }
        }
        if (s.substring(s.length() - 1, s.length()).equals(" ")) {
            return answer + " ";
        }
        
        return answer;
    }
}