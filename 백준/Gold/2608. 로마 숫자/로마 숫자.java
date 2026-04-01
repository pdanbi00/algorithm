import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String num1 = br.readLine();
        String num2 = br.readLine();

        int[] nums = new int[] {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] chars = new String[] {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        Map<Integer, String> numMap = new HashMap<>();
        Map<String, Integer> charMap = new HashMap<>();
        Set<String> check = new HashSet<>(Arrays.asList("V", "L", "D", "IV", "IX", "XL", "XC", "CD", "CM"));
        for (int i = 0; i < nums.length; i++) {
            numMap.put(nums[i], chars[i]);
            charMap.put(chars[i], nums[i]);
        }

        int n1 = 0;
        int n = num1.length();
        int idx = 0;
        while (idx < n) {
            String p = String.valueOf(num1.charAt(idx));
            if (idx < n-1) {
                String tmp = num1.substring(idx, idx+2);
                if (check.contains(tmp)) {
                    n1 += charMap.get(tmp);
                    idx += 2;
                } else {
                    n1 += charMap.get(p);
                    idx += 1;
                }
            } else {
                n1 += charMap.get(p);
                idx += 1;
            }
        }

        int n2 = 0;
        n = num2.length();
        idx = 0;
        while (idx < n) {
            String p = String.valueOf(num2.charAt(idx));
            if (idx < n-1) {
                String tmp = num2.substring(idx, idx+2);
                if (check.contains(tmp)) {
                    n2 += charMap.get(tmp);
                    idx += 2;
                } else {
                    n2 += charMap.get(p);
                    idx += 1;
                }
            } else {
                n2 += charMap.get(p);
                idx += 1;
            }
        }

        int total = n1 + n2;
        System.out.println(total);

        String answer = "";
        Set<String> used = new HashSet<>();
        for (int k : nums) {
            int cnt = 0;
            String target = numMap.get(k);
            while (total >= k) {
                if (check.contains(target) && used.contains(target)) break;

                if (cnt >= 3) break;

                n = answer.length();
                if (n >= 2) {
                    if (target.equals("IV") && answer.substring(n-2, n).equals("IX")) {
                        break;
                    } else if (target.equals("XL") && answer.substring(n-2, n).equals("XC")) {
                        break;
                    } else if (target.equals("CM") && answer.substring(n-2, n).equals("CD")) {
                        break;
                    }
                }


                total -= k;
                answer += "" + target;
                used.add(target);
                cnt++;
            }
        }

        System.out.print(answer);
    }
}
