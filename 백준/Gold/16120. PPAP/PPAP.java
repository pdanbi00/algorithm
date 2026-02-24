import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String target = br.readLine();
        String answer = "NP";
        String ppap = "PAPP";

        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < target.length(); i++) {
            stack.add(target.charAt(i));
            if (stack.size() >= 4) {
                boolean possible = true;
                for (int j = 0; j < 4; j++) {
                    if (stack.get(stack.size()-1-j) != ppap.charAt(j)) {
                        possible = false;
                        break;
                    }
                }
                if (possible) {
                    for (int j = 0; j < 3; j++) {
                        stack.pop();
                    }
                }
            }
        }
        if (stack.size() == 1 && stack.get(0) == 'P') {
            answer = "PPAP";
        }
        System.out.print(answer);
    }
}
