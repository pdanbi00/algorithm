import java.util.Map;
import java.util.HashMap;
class Solution {
    public String solution(String letter) {
        String answer = "";
        Map<String, Character> map = new HashMap<>(){{
            put(".-", 'a');
            put("-...", 'b');
            put("-.-.", 'c');
            put("-..", 'd');
            put(".", 'e');
            put("..-.", 'f');
            put("--.", 'g');
            put("....", 'h');
            put("..", 'i');
            put(".---", 'j');
            put("-.-", 'k');
            put(".-..", 'l');
            put("--", 'm');
            put("-.", 'n');
            put("---", 'o');
            put(".--.", 'p');
            put("--.-", 'q');
            put(".-.", 'r');
            put("...", 's');
            put("-", 't');
            put("..-", 'u');
            put("...-", 'v');
            put(".--", 'w');
            put("-..-", 'x');
            put("-.--", 'y');
            put("--..", 'z');
        }};
        String[] letterArray = letter.split(" ");
        for (int i = 0; i < letterArray.length; i++) {
            answer += map.get(letterArray[i]);
        }
        
        return answer;
    }
}