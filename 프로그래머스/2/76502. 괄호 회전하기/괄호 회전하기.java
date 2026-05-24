import java.util.Stack;
class Solution {
    public int solution(String s) {
        int answer = 0;
        int N = s.length();
        for (int i = 0; i < N; i++) {
            String tmp = s.substring(i, N) + s.substring(0, i);
            boolean possible = true;
            Stack<Character> stack = new Stack<>();
            for (int j = 0; j < N; j++) {
                if (tmp.charAt(j) == '{' || tmp.charAt(j) == '(' || tmp.charAt(j) == '[') {
                    stack.push(tmp.charAt(j));
                } else if (tmp.charAt(j) == '}') {
                    if (!stack.isEmpty() && stack.peek() == '{') {
                        stack.pop();
                    } else {
                        possible = false;
                        break;
                    }
                } else if (tmp.charAt(j) == ')') {
                    if (!stack.isEmpty() && stack.peek() == '(') {
                        stack.pop();
                    } else {
                        possible = false;
                        break;
                    }
                } else if (tmp.charAt(j) == ']') {
                    if (!stack.isEmpty() && stack.peek() == '[') {
                        stack.pop();
                    } else {
                        possible = false;
                        break;
                    }
                }
            }
            
            if (possible && stack.isEmpty()) {
                answer++;
            }
        }
        return answer;
    }
}